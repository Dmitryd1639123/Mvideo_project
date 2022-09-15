from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hlink
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from tg_mv_funcs import sql_result, sql_find_all, users_clicks, id, name, lstName, nick
from states import Search
from time import sleep
import mvideo_buttons as mv
import os

# -- Bot ---
bot = Bot(token=os.getenv('TG_MVIDEO_BOT'), parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def on_shutdown(dp):
     await bot.close()
     await storage.close()


# --- Handlers ---
@dp.message_handler(commands='find', state=None)
async def enter_test(message: types.Message):
     await message.answer("Введите полное или частичное название товара: ")
     await Search.Find.set()


@dp.message_handler(state=Search.Find)
async def find_goods(message: types.Message, state: FSMContext):

     answer = message.text
     await state.update_data(answer1 = answer)
     await message.answer('Processing...')

     if message.text:

          count = 0
          goods = sql_find_all(product = message.text)

          try:
               for index, item in enumerate(goods):
                    card = f"{ hlink(item[0], item[4]) }\n"\
                         f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                         f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                         f"{ hbold('Старая цена: ')}{ item[1]}        "\
                         f"{ hbold('Бонусы: ')}{ item[3] }"

                    count += 1
               
                    if index % 20 == 0:
                         sleep(3)

                    await message.answer(card)

          except Exception:
               await message.answer('Произошла ошибка! Попробуйте ввести запрос еще раз, или повтортие попытку позже!')

          await message.answer(f'Найдено товаров: {count}.\nДля повторого поиска воспользуйтесь командой "/find".')  

     await state.finish()

     users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
     f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')


@dp.message_handler(commands='start')
async def start(message: types.Message):
     await message.answer('Выберите категорию, {0.first_name}'.format(message.from_user), reply_markup=mv.mainMenu)


# --- Buttons ---
@dp.message_handler()
async def goods_buttons(message: types.Message):

     global mainBtn
#                                       --- Смартфоны и связь ---
     if message.text == '📱Смартфоны':
          mainBtn = '📱Смартфоны'
          await bot.send_message(message.from_user.id, '📱Смартфоны', reply_markup=mv.smartphonesMenu)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Apple ---
     elif message.text == 'Apple' and mainBtn == '📱Смартфоны':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'APPLE'", main_category = "'Смартфоны и связь'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Xiaomi ---
     elif message.text == 'Xiaomi' and mainBtn == '📱Смартфоны':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'XIAOMI'", main_category = "'Смартфоны и связь'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена: ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}      "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')               

# --- Samsung ---
     elif message.text == 'Samsung' and mainBtn == '📱Смартфоны':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'SAMSUNG'", main_category = "'Смартфоны и связь'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена: ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}      "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')               

# --- Realme ---
     elif message.text == 'Realme' and mainBtn == '📱Смартфоны':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'REALME'", main_category = "'Смартфоны и связь'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена: ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}      "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Huawei ---
     elif message.text == 'Huawei' and mainBtn == '📱Смартфоны':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'HUAWEI'", main_category = "'Смартфоны и связь'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена: ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}      "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Tecno ---
     elif message.text == 'Tecno' and mainBtn == '📱Смартфоны':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'TECNO'", main_category = "'Смартфоны и связь'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена: ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}      "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Vivo ---
     elif message.text == 'Vivo' and mainBtn == '📱Смартфоны':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'VIVO'", main_category = "'Смартфоны и связь'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена: ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}      "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Прочее ---
     elif message.text == 'Прочее' and mainBtn == '📱Смартфоны':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'APPLE', 'XIAOMI', 'SAMSUNG', 'REALME', 'HUAWEI', 'TECNO', 'VIVO'",\
                main_category = "'Смартфоны и связь'", contain='NOT IN', comment='--')

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена: ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}      "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')
                    

     elif message.text == '⬅️Главное меню':
          await bot.send_message(message.from_user.id, '⬅️Главное меню', reply_markup=mv.mainMenu)
     
          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')



#                                       --- ТЕЛЕВИЗОРЫ И ЦИФРОВОЕ ТВ ---
     elif message.text == '📺Телевизоры':
          mainBtn = '📺Телевизоры'
          await bot.send_message(message.from_user.id, '📺Телевизоры', reply_markup=mv.tvMenu)
          
          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Sony ---    
     elif message.text == 'Sony' and mainBtn == '📺Телевизоры':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'SONY'", main_category = "'ТЕЛЕВИЗОРЫ И ЦИФРОВОЕ ТВ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Samsung ---      
     elif message.text == 'Samsung' and mainBtn == '📺Телевизоры':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'SAMSUNG'", main_category = "'ТЕЛЕВИЗОРЫ И ЦИФРОВОЕ ТВ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- LG ---      
     elif message.text == 'LG' and mainBtn == '📺Телевизоры':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'LG'", main_category = "'ТЕЛЕВИЗОРЫ И ЦИФРОВОЕ ТВ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Philips ---      
     elif message.text == 'Philips' and mainBtn == '📺Телевизоры':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'PHILIPS'", main_category = "'ТЕЛЕВИЗОРЫ И ЦИФРОВОЕ ТВ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Telefunken ---      
     elif message.text == 'Telefunken' and mainBtn == '📺Телевизоры':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'TELEFUNKEN'", main_category = "'ТЕЛЕВИЗОРЫ И ЦИФРОВОЕ ТВ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Haier ---      
     elif message.text == 'Haier' and mainBtn == '📺Телевизоры':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'HAIER'", main_category = "'ТЕЛЕВИЗОРЫ И ЦИФРОВОЕ ТВ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Hisense ---      
     elif message.text == 'Hisense' and mainBtn == '📺Телевизоры':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'HISENSE'", main_category = "'ТЕЛЕВИЗОРЫ И ЦИФРОВОЕ ТВ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Прочее ---      
     elif message.text == 'Прочее' and mainBtn == '📺Телевизоры':
          await message.answer('Processing...')

          data = sql_result(manufacturers = "'SONY','SAMSUNG','LG','PHILIPS','TELEFUNKEN','HAIER','HISENSE'",\
                main_category = "'ТЕЛЕВИЗОРЫ И ЦИФРОВОЕ ТВ'", contain='NOT IN', comment = '--')

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')


#                                       --- КОМПЬЮТЕРНАЯ ТЕХНИКА ---

     elif message.text == '💻Компьютерная техника':
          mainBtn = '💻Компьютерная техника'
          await bot.send_message(message.from_user.id, '💻Компьютерная техника', reply_markup=mv.compMenu)
          
          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Ноутбуки ---    
     elif message.text == 'Ноутбуки' and mainBtn == '💻Компьютерная техника':
          await message.answer('Processing...')

          data = sql_result(subcategory = "'ИГРОВЫЕ НОУТБУКИ', 'НОУТБУКИ', 'НОУТБУКИ APPLE MACBOOK', 'НОУТБУКИ-ТРАНСФОРМЕРЫ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Планшеты ---    
     elif message.text == 'Планшеты' and mainBtn == '💻Компьютерная техника':
          await message.answer('Processing...')

          data = sql_result(subcategory = "'ПЛАНШЕТЫ НА ANDROID'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Системные блоки ---    
     elif message.text == 'Системные блоки' and mainBtn == '💻Компьютерная техника':
          await message.answer('Processing...')

          data = sql_result(subcategory = "'СИСТЕМНЫЕ БЛОКИ', 'СИСТЕМНЫЕ БЛОКИ ИГРОВЫЕ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Мониторы ---    
     elif message.text == 'Мониторы' and mainBtn == '💻Компьютерная техника':
          await message.answer('Processing...')

          data = sql_result(subcategory = "'МОНИТОРЫ', 'ИГРОВЫЕ МОНИТОРЫ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')


#                                       --- "Электротранспорт" ---

     elif message.text == '🛴Электротранспорт':
          mainBtn = '🛴Электротранспорт'
          await bot.send_message(message.from_user.id, '🛴Электротранспорт', reply_markup=mv.eltrMenu)
          
          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Самокаты ---    
     elif message.text == 'Самокаты' and mainBtn == '🛴Электротранспорт':
          await message.answer('Processing...')

          data = sql_result(subcategory = "'ЭЛЕКТРОСАМОКАТЫ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Гироскутеры ---    
     elif message.text == 'Гироскутеры' and mainBtn == '🛴Электротранспорт':
          await message.answer('Processing...')

          data = sql_result(subcategory = "'ГИРОСКУТЕРЫ 10 ДЮЙМОВ', 'ГИРОСКУТЕРЫ 8 ДЮЙМОВ', 'ГИРОСКУТЕРЫ 6.5 ДЮЙМОВ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Велосипеды ---    
     elif message.text == 'Велосипеды' and mainBtn == '🛴Электротранспорт':
          await message.answer('Processing...')

          data = sql_result(subcategory = "'ЭЛЕКТРОВЕЛОСИПЕДЫ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

# --- Аксессуары ---    
     elif message.text == 'Аксессуары' and mainBtn == '🛴Электротранспорт':
          await message.answer('Processing...')

          data = sql_result(subcategory = "'АКСЕССУАРЫ ДЛЯ ГИРОСКУТЕРОВ'")

          for index, item in enumerate(data):
               card = f"{ hlink(item[0], item[4]) }\n"\
                    f"{ hbold('Новая цена:   ')}{item[2]}🔥  "\
                    f"{ hbold('Рейтинг: ')}{ item[5] }🌟\n"\
                    f"{ hbold('Старая цена: ')}{ item[1]}        "\
                    f"{ hbold('Бонусы: ')}{ item[3] }"
               
               if index % 20 == 0:
                    sleep(3)

               await message.answer(card)

          users_clicks(f'{id.format(message.from_user)}',f'{nick.format(message.from_user)}',f'{name.format(message.from_user)}',\
               f'{lstName.format(message.from_user)}',f'{message.text.format(message.from_user)}')

def main():
     
     executor.start_polling(dp, on_shutdown=on_shutdown)

if __name__ == '__main__':
     main()




#
                    
  
               
