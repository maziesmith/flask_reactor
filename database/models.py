from sqlalchemy import Column, Integer, String, Float, UniqueConstraint
from .database import Base


# Element model
class Element(Base):
    __tablename__="element"
    id = Column(Integer, primary_key=True, index=True)
    ele = Column(String)
    weight = Column(Float)
    grouping = Column(String)
    phase = Column(String)
    period = Column(Integer)
    config = Column(String)
    melting = Column(Float)
    boiling = Column(Float)
    symbol = Column(String)
    __table_args__ = (UniqueConstraint('ele'),)

# Daily element model
class Daily(Base):
    __tablename__="daily"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String)

# Industry news model
class News(Base):
    __tablename__="news"
    id = Column(Integer, primary_key=True, index=True)
    link = Column(String)
    text = Column(String)