from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class DomainEntityAction(Model):
    
    idDomainEntityAction = Column(Integer, primary_key=True)
    name = Column(String(150), unique = True, nullable=False)
    description =  Column(String(564), default='Description: ')
    parameters = Column(String(20))
    returnLiteral = Column(String(20))
    domentity_id = Column(String(20))
    domentity = Column(String(20))


    def __repr__(self):
        return self.name

"""
    domainentity_id = Column(Integer, ForeignKey('domainentity.idEntity'))
    domainentity = relationship("DomainEntity")
"""