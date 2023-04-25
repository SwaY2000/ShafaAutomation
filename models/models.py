from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///mydatabase.db')
Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)


class Photo(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    product_id = Column(Integer, ForeignKey('products.id'))

Base.metadata.create_all(engine)