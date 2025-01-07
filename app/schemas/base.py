from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """
    Базовый класс для всех схем
    """

    model_config = ConfigDict(from_attributes=True)
