from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class Actor(Model):
    
    idActor = Column(Integer, primary_key=True)
    name = Column(String(150), unique = True, nullable=False)
    description = Column(String(564), default='Description: ')
    requirement_has_Actor = Column(String(20))

    def __repr__(self):
        return self.name