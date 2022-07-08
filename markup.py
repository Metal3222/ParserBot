from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#---main menu---
btnOne = KeyboardButton("Поиск")
btnTwo = KeyboardButton("Меню пользователя")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOne, btnTwo)

#---work menu---
btnOne = KeyboardButton("Сортировка")
btnTwo = KeyboardButton("Что-то еще")
workMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOne, btnTwo)

#---user menu---
btnOne = KeyboardButton("Статус")
btnTwo = KeyboardButton("Купить подписку")
userMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOne, btnTwo)