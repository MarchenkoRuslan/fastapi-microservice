from sqlalchemy.ext.declarative import declarative_base


class CustomBase:
    """Базовый класс для всех моделей."""
    __name__: str
    # Общие поля и методы для всех моделей можно добавить здесь


Base = declarative_base(cls=CustomBase) 