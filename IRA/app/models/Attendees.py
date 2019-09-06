from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class Attendees(Model):
    
    idAttendees = Column(Integer, primary_key=True)
    name = Column(String(150), unique = True, nullable=False)
    email = Column(String(564), default='Emails: ')
    minutesOfMeetings_has_Attendees = Column(String(20))

    def __repr__(self):
        return self.name