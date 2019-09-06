from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship



class MinutesOfMeetings(Model):
    
    idMinutesOfMeeting = Column(Integer, primary_key=True)
    starttime = Column(String(20))
    meetingLink = Column(String(20))
    endtime = Column(String(20))
    location = Column(String(20))
    subject = Column(String(20))
    agenda = Column(String(20))
    moM = Column(String(20))
    actionItems = Column(String(20))
    idText = Column(Integer, ForeignKey('text.idText'))
    text = relationship("Text")        
    minutesOfMeetings_has_Attendees = Column(String(564), default='List of Attendees: ')

    def __repr__(self):
        return self.name