from app.db.base_class import Base
from app.models.client import Client
from app.models.order import Order
from app.models.profile import Profile
from app.models.survey import Survey
from app.models.verification import Verification

# Импортируем все модели здесь, чтобы Alembic мог их найти
__all__ = ["Base", "Client", "Order", "Profile", "Survey", "Verification"] 