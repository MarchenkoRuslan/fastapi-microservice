from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """
    Базовый класс для всех схем в приложении
    """

    model_config = ConfigDict(from_attributes=True)
