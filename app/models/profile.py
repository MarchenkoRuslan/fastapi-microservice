from uuid import uuid4

from sqlalchemy import UUID, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Profile(Base):
    id = Column(UUID, primary_key=True, default=uuid4)
    name = Column(String)
    client_id = Column(UUID, ForeignKey("client.id"))
    client = relationship("Client", back_populates="profiles")
