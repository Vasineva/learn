
"""
Модуль предназначен для запуска телеграм-бота.

Использует библиотеку `telepot` для взаимодействия с API Telegram и обработки входящих сообщений через функцию `handle_message`.

Функциональность:
- Инициализация бота с использованием токена.
- Запуск цикла обработки сообщений.
- Логирование событий, включая успешный запуск и ошибки.

Перед использованием:
1. Убедитесь, что токен указан в файле `config.py`.
2. Проверьте, что в папке `PIC` находятся необходимые изображения:
   - `start.jpg`
   - `programm.jpg`
   - `feedbacks.jpg`
   - `victorina.jpg`
"""

import telepot
import logging
from telepot.loop import MessageLoop
from config import TOKEN
from handlers import handle_message

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

bot = telepot.Bot(TOKEN)
# Запуск цикла обработки сообщений. При поступлении сообщения вызывается функция handle_message
MessageLoop(bot, lambda msg: handle_message(msg, bot)).run_as_thread()
logging.info("Бот успешно запущен и ожидает сообщений.")

# Бесконечный цикл, чтобы бот продолжал работать. Пока нет других задач, используется pass.
while True:
    pass