import os
import logging
from web import main

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        # Запускаем веб-сервер
        main()
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        raise 