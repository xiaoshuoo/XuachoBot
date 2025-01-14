from pathlib import Path
from typing import Dict, List

# Базовые настройки
BASE_DIR = Path(__file__).parent
LOGS_DIR = BASE_DIR / "logs"
TEMP_DIR = BASE_DIR / "temp"

# Настройки бота
BOT_CONFIG = {
    "max_conversations": 1000,
    "session_timeout": 3600,
    "max_retries": 3
}

# Настройки файлов
FILE_CONFIG = {
    "max_size": 20 * 1024 * 1024,
    "max_image_size": 10 * 1024 * 1024,
    "allowed_types": {
        "image": [".jpg", ".jpeg", ".png", ".webp"],
        "document": [".pdf", ".doc", ".docx", ".txt"],
        "spreadsheet": [".xlsx", ".xls", ".csv"]
    }
}

# Языковые настройки
LANGUAGE_CONFIG = {
    "default": "ru",
    "supported": ["ru", "en", "es", "de"]
} 