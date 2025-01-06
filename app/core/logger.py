import logging
from logging.handlers import RotatingFileHandler
import sys
from pathlib import Path

# Создаем директорию для логов если её нет
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Настраиваем форматирование
log_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Файловый handler
file_handler = RotatingFileHandler(
    log_dir / "app.log", maxBytes=10485760, backupCount=5  # 10MB
)
file_handler.setFormatter(log_formatter)

# Консольный handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_formatter)

# Настраиваем корневой logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
root_logger.addHandler(file_handler)
root_logger.addHandler(console_handler)

# Создаем logger для приложения
logger = logging.getLogger("app")
