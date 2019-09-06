from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class SubDomain(Model):
    
    idSubDomain = Column(Integer, primary_key=True)
    name = Column(String(150), unique = True, nullable=False)
    description =  Column(String(564), default='Description: ')
    domainArchitecture = Column(String(55), default='Arch')
    requirement_has_SubDomain = Column(String(20))
    domain_id = Column(Integer, ForeignKey('domain.id'))
    domain = relationship("Domain")
    subDomain_has_Entities = Column(String(20))

    def __repr__(self):
        return self.name