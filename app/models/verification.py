from uuid import uuid4

from sqlalchemy import UUID, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Verification(Base):
    id = Column(UUID, primary_key=True, default=uuid4)
    status = Column(String)
    client_id = Column(UUID, ForeignKey("client.id"))
    order_id = Column(UUID, ForeignKey("order.id"))

    client = relationship("Client", back_populates="verifications")
    order = relationship("Order", back_populates="verifications")
