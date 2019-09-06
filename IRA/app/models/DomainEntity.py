from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class DomainEntity(Model):
    
    idEntity = Column(Integer, primary_key=True)
    name = Column(String(150), unique = True, nullable=False)
    description = Column(String(564), default='Domain Entity: ')
    domainEntityAction = Column(String(564), default='Action: ')
    domainEntityAttributes = Column(String(564), default='Attributes: ')
    subDomain_has_Entities = Column(String(20))
    text_has_DomainEntities = Column(String(20))

    def __repr__(self):
        return self.name