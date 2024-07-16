from engine.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class UserProfile(Base):
    __tablename__ = 'crickter'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(225), nullable=False)
    country = Column(String(225), nullable=False)
    age = Column(String(225), nullable=False)
    profile = relationship('RunTable', back_populates='runs')
    strike_rate = relationship('StrikeRate', back_populates='strike')


class RunTable(Base):
    __tablename__ = 'runtable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('crickter.id'), nullable=False)
    ODI = Column(Integer, nullable=False)
    T20 = Column(Integer, nullable=False)
    Test = Column(Integer, nullable=False)
    runs = relationship('UserProfile', back_populates='profile')


class StrikeRate(Base):
    __tablename__ = 'strike_rate'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('crickter.id'), nullable=False)
    ODI = Column(Float, nullable=False)
    T20 = Column(Float, nullable=False)
    Test = Column(Float, nullable=False)
    strike = relationship('UserProfile', back_populates='strike_rate')
