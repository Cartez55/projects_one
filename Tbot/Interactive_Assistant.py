import requests
from aiogram import Bot,Dispatcher, executor
from Config import BOT_TOKEN
import asyncio

# Old code using GET request
# # Получаем апдейт с последним сообщением
# update = requests.get(API_link + '/getUpdates?offset=-1').json()
# message = update['result'][0]['message']
# chat_id = message['from']['id']
# text = message['text']
# send_message = requests.get(API_link + f'/sendMessage?chat_id={chat_id}&text=Привет, ты написал {text}')

# Current code
# Получение потока
loop = asyncio.get_event_loop()
# Класс бота, содержащий бот токен
bot = Bot(BOT_TOKEN, parse_mode='HTML')
# Обработчик и доставщик: содержит бота и поток
dispatcher = Dispatcher(bot, loop=loop)

# Код выполнится только если, мы запускаем файл, а не импортируем
if __name__ == "__main__":
    # Испортируем обработчик и функцию send_to_admin
    from handler import dispatcher, send_to_admin
    # Автоматическая доставка сообщений от клиента и автоматический get.Update
    # On_startup - функция запуска бота, при запуске бота будет запускаться функция send_to_admin
    executor.start_polling(dispatcher, on_startup=send_to_admin)