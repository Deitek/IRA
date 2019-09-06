from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class ProductFeatures(Model):
    
    idProductFeature = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)
    description = Column(String(564), default='Product Feature ')
    product_has_ProductFeatures = Column(String(20))
    requirement_id = Column(Integer, ForeignKey('requirements.id'))
    requirement = relationship("Requirements")

    def __repr__(self):
        return self.name