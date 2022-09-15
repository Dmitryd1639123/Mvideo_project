import requests
from pg_connect import postgres
from time import sleep
from params import cookies, headers, params, categories

# Список JSON'ов из которых будем тянуть инфу
api_listing = 'https://www.mvideo.ru/bff/products/listing'
api_list = 'https://www.mvideo.ru/bff/product-details/list'
api_prices = 'https://www.mvideo.ru/bff/products/prices'

products = {}  # Создаем словарь где ключом будет код товара, а занчением список с необходимыми атрибутами
params['offset']  = int( params['offset'] )            
params['categoryId']  = int( params['categoryId'] )    # значения  params['offset'] и int( params['categoryId']  периодически меняют тип данных. Приравнием к INT


def main():

     print('\n[MESSAGE]: Start download\n')
     s = requests.Session()

     # Основной цикл, перебирает категории товаров
     for category in categories:             
          params['categoryId'] = category

          #Цикл перебора страниц категорий
          while True:
               # Пробуем забирать информацию через API
               try:
                    # Забираем коды товаров
                    response = s.get(api_listing, params=params, cookies=cookies, headers=headers).json()
                    current_category = response['body']['currentCategory']['name']

                    # Записываеи коды в переменную
                    product_codes = response['body']['products']

                    # Вставляем коды в слуд. переменную для следующего обращения, через которое вытаскиваем информацию о товарах (кроме цен, баллов и т.п)
                    json_data = {'productIds': product_codes,'mediaTypes':['images'],'category':True,'status':True,'brand':True,'propertyTypes':['KEY'],\
                         'propertiesConfig':{'propertiesPortionSize':5},'multioffer':False}

                    #Запрашиваем информацию о товаре по их кодам сохраненных в переменно
                    response = s.post(api_list, cookies=cookies, headers=headers, json=json_data).json()

                    # Записываем характеристики товара в словарь в виде списка
                    try:
                         for product in response['body']['products']:
                              # проставляем 0 для товаров без оценок
                              if  product['rating']['star'] == None:
                                   product['rating']['star'] = 0
                              # На всякий случай проводим аналогичное действие для "Производителя"
                              if product['brandName'] == None:
                                   product['brandName'] = 'Not found'

                              products[product['productId']] = [ product['name'], current_category, product['category']['name'],
                              f"https://www.mvideo.ru/products/{product['productId']}",  product['brandName'], product['rating']['star'] ]

                    # В случае ошибки связанной с полученной информацией, выводим ошибку и приступаем к след. итерации
                    except KeyError as er:
                         print(er)
                         continue

                    # Переводим словарь из кодов товаров в строку, так как именно такой формат нужен в следующем обращении
                    product_codes_str = ','.join(product_codes)

                    params_for_prices = {
                    'productIds': product_codes_str,
                    'addBonusRubles': 'true',
                    'isPromoApplied': 'true',
                    }
                    
                    #Запрашиваем информацию о ценах товаров
                    response = s.get(api_prices, params=params_for_prices, cookies=cookies, headers=headers).json()

               # В случае если нас заблочили выводим текст, добавляем категорию с ошибкой в конец списка что пройти по ней в конце. Ставим таймаут на 100 сек.
               except requests.exceptions.JSONDecodeError:
                    print('[ERROR]: The server blocked the request. Parsing of this category has been moved to the end. A timeout of 100 seconds is executed')
                    categories.append(category)
                    sleep(100)

               # Добавляем к словарю данные о ценах, записываем информацию в PostgreSQL
               try:

                    for price in response['body']['materialPrices']:
                         x = price['productId']
                         y = products[x]
                         base_price = price['price']['basePrice']
                         sale_price = price['price']['salePrice']
                         bonus_rubles = price['bonusRubles']['total']

                         products[x] == y.append(base_price)
                         products[x] == y.append(sale_price)
                         products[x] == y.append(bonus_rubles)

                         postgres(query=f"""

                         insert into mvideo_products(prd_id, main_cat_id, main_cat_name,       
                         sec_cat_name, load_dttm, load_dt, prd_name, base_price, sale_price, cashback, prd_url, manufacturer, prd_stars)    

                         values({x}, {category},  '{current_category}', '{products[x][2]}', current_timestamp, current_date, '{products[x][0]}',
                          {base_price}, {sale_price}, {bonus_rubles}, '{products[x][3]}', '{products[x][4]}', round({products[x][5]},1))     
                         
                         """) 
                         
               # Если категория отсутствует или в ней нет товаров со скидками(или нет товара в наличии). Выводим текст обнуляем номер страницы.
               except KeyError:
                    if len(products) % 24 == 0 :

                         print(f"""[+]: #{params['categoryId']} category: "{current_category}" loaded successfully! Goods count: {len(products)}""")
                         params['offset'] = 0
                         break

               # Если кол-во товаров кратно "24" - переходим на след. страницу. P.S. (на странице 24 поз.)   
               if len(products) % 24 == 0:
                    params['offset'] += 24      

               # Если кол-во товаров перестало быть кратной "24" значит страницы закончились. Чистим переменную со списком Выходим из цикла. Таймаут 5 сек     
               else:   
                    print(f"""[+]: #{params['categoryId']} category: "{current_category}" loaded successfully! Goods count: {len(products)}""")
                    params['offset'] = 0
                    products.clear()
                    break 
          sleep(5)

     #Удяляем из БД все дубли товаров в разрезе текущего дня. Оставляем более позднюю загрузку.
     postgres(query=
          """
          delete from mvideo_products
          where (prd_id, load_dttm) in (
                                        select prd_id, load_dttm from (
                                                  select 
                                                         prd_id
                                                       , load_dttm
                                                       , row_number() over(partition by prd_id, load_dt order by load_dttm desc) as rn
                                                  from mvideo_products where load_dt = current_date 
                                        )a
                                        where rn != 1
          )
          and load_dt = current_date;
          """
     )

     print('\n[MESSAGE]: Loading is complete!\n')   
     return products

if __name__ == "__main__":
     main()
