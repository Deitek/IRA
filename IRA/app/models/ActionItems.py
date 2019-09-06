from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship



class ActionItems(Model):
    
    idActionItem = Column(Integer, primary_key=True)
    description =  Column(String(564), default='Description: ')
    idMinutesOfMeeting = Column(String(20))

    def __repr__(self):
        return self.name