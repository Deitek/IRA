from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class EmailRequirements(Model):
    
    idEmailRequirement = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    subject = Column(String(564), default='Subject ')
    text = Column(String(564), default='Text: ')
    sender = Column(String(200))
    requirement_has_EmailRequirements = Column(String(20))

    def __repr__(self):
        return self.name