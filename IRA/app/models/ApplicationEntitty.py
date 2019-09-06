from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class ApplicationEntitty(Model):
    
    idApplicationEntitty = Column(Integer, primary_key=True)
    name = Column(String(150), unique = True, nullable=False)
    description = Column(String(564), default='Description: ')
    applicationEntitty_has_Requirement = Column(String(20))
    applicationEntityActions = Column(String(20))
    applicationEntityAttributes = Column(String(20))
    text_has_ApplicationEntitty = Column(String(20))

    def __repr__(self):
        return self.name
