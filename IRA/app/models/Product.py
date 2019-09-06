from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship

class Product(Model):
    
    idProduct = Column(Integer, primary_key=True)
    name = Column(String(150), unique = True, nullable=False)
    description = Column(String(564), default='The Product: ')
    product_has_ProductFeatures = Column(String(20))

    def __repr__(self):
        return self.name