import asyncio
import os
from telegram import main

if __name__ == "__main__":
    # Получаем порт из переменной окружения или используем значение по умолчанию
    port = int(os.environ.get("PORT", 10000))
    
    # Запускаем бота
    asyncio.run(main()) 