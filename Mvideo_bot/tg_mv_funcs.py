from pg_connect import postgres

# Записываем в переменные информацию о пользователе
id = ('{0.id}')
nick = ('{0.username}')
name = ('{0.first_name}')
lstName = ('{0.last_name}')


def day_selection():
     """Функция выбирает день, за который бот будет отправлять товары. Необходио для работы бота, в случае если за сегодня не было загрузки товаров в БД"""
     count = postgres(
               """
               select count(*) from mvideo_products
               where load_dt = current_date;
               """
     )

     if count[0][0] > 0:
          day = 'current_date'
     else:
          day = 'current_date - 1'
     
     return day


def sql_result(manufacturers = "UPPER(MANUFACTURER)", main_category = "MAIN_CAT_NAME", subcategory = "UPPER(SEC_CAT_NAME)", contain = "IN", comment = ''):
     """Функция выборки товаров для кнопок бота"""
     result = postgres(
               f"""
               SELECT DISTINCT
                    PRD_NAME
                    , BASE_PRICE
                    , SALE_PRICE
                    , CASHBACK
                    , PRD_URL
                    , PRD_STARS
                    , BASE_PRICE / SALE_PRICE
               FROM MVIDEO_PRODUCTS
               WHERE 1=1
               AND UPPER(MANUFACTURER) {contain} ({manufacturers})
               AND LOAD_DT = {day_selection()}
               AND UPPER(MAIN_CAT_NAME) = UPPER({main_category})
      {comment}AND UPPER(SEC_CAT_NAME) {contain} ({subcategory})
               ORDER BY SALE_PRICE, BASE_PRICE / SALE_PRICE
               """
     )
     return result


def sql_find_all(product = ''):
     """Функция выборки товаров для ручного поиска товаров бота. (Команда '/find')"""
     result = postgres(
               f"""
               SELECT DISTINCT
                    PRD_NAME
                    , BASE_PRICE
                    , SALE_PRICE
                    , CASHBACK
                    , PRD_URL
                    , PRD_STARS
                    , BASE_PRICE / SALE_PRICE
               FROM MVIDEO_PRODUCTS
               WHERE 1 = 1
               AND LOAD_DT = {day_selection()}
               AND UPPER(PRD_NAME) LIKE(UPPER('%{product}%'))
               ORDER BY SALE_PRICE, BASE_PRICE / SALE_PRICE
               """
     )
     return result


def users_clicks(id, nick, name, lstName, button):
     """Функция сбора и записи данных / действий пользователя в БД"""
     postgres(     
     f"""
     insert into user_clicks(load_dttm, load_dt, user_id, nickname, first_name, last_name, button_name)    
     values(current_timestamp, current_date, '{id}', '{nick}', '{name}', '{lstName}', '{button}')  
     """
     )

 
if __name__ == '__main__':
     sql_result()
     