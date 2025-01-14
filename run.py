import asyncio
import os
import logging
from telegram import main

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        # Получаем порт из переменной окружения
        port = int(os.environ.get("PORT", 10000))
        logger.info(f"Starting bot on port {port}")
        
        # Проверяем наличие необходимых переменных окружения
        required_vars = ["TELEGRAM_TOKEN", "GEMINI_API_KEY"]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
            raise ValueError(f"Please set the following environment variables: {', '.join(missing_vars)}")
        
        # Запускаем бота
        asyncio.run(main())
        
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise 