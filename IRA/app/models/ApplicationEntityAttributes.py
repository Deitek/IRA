from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class ApplicationEntityAttributes(Model):
    
    idApplicationEntityAttribute = Column(Integer, primary_key=True)
    name = Column(String(150), unique = True, nullable=False)
    description =  Column(String(564), default='Description: ')
    defaultvalue = Column(String(20))
    dataType = Column(String(20))
    idApplicationEntity = Column(String(20))

    def __repr__(self):
        return self.name