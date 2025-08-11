import logging

# Налаштовуємо конфігурацію логування один раз
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Отримуємо об'єкт-логер для використання
logger = logging.getLogger(__name__)
