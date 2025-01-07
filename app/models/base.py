from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    """
    Базовый класс для всех моделей SQLAlchemy
    """

    @declared_attr
    def __tablename__(cls) -> str:
        """
        Автоматически генерирует имя таблицы из имени класса
        """
        return cls.__name__.lower()
