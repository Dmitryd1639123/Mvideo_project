from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --- Cancel Button ---
cancelBtn = KeyboardButton('⬅️Главное меню')

# --- Main Menu ---
mainBtns = ['📱Смартфоны', '📺Телевизоры', '💻Компьютерная техника', '🛴Электротранспорт']
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(*mainBtns)


# --- Smartphones Menu ---
smartphonesBtns = ['Apple', 'Xiaomi', 'Samsung', 'Realme', 'Huawei', 'Tecno', 'Vivo', 'Прочее', cancelBtn]
smartphonesMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(*smartphonesBtns)


# --- TV Menu ---
tvBtns = ['Sony', 'Samsung', 'LG', 'Philips', 'Telefunken', 'Haier', 'Hisense', 'Прочее', cancelBtn]
tvMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(*tvBtns)


# --- Computer Technology ---
compBtns = ['Ноутбуки', 'Планшеты', 'Системные блоки', 'Мониторы', cancelBtn]
compMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(*compBtns)


# --- Electro transport ---
eltrBtns = ['Самокаты', 'Гироскутеры', 'Велосипеды', 'Аксессуары', cancelBtn]
eltrMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(*eltrBtns)


