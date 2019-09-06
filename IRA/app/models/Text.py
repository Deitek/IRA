from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class Text(Model):
    
    idText = Column(Integer, primary_key=True)
    name = Column(String(150), unique = True, nullable=False)
    text = Column(String(564), default='text: ')
    minutesOfMeetings = Column(String(564), default='Mom: ')
    requirement_id = Column(Integer, ForeignKey('requirements.id'))
    requirement = relationship("Requirements")
    text_has_ApplicationEntitty = Column(String(20))
    text_has_DomainEntities = Column(String(20))

    def __repr__(self):
        return self.name