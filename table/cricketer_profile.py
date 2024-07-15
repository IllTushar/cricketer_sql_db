from engine.database import Base
from sqlalchemy import Column, Integer, String


class UserProfile(Base):
    __tablename__ = 'crickter'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(225), nullable=False)
    country = Column(String(225), nullable=False)
    age = Column(String(225), nullable=False)
