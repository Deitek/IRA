from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship



class Domain(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)
    description = Column(String(564), default='Dominio ')
    subDomain = Column(String(564), default='Subdomain')

    def __repr__(self):
        return self.name

class Requirements(Model):
    id = Column(Integer, primary_key=True)
    name =  Column(String(150), unique = True, nullable=False)
    description =  Column(String(564), default='El sistema debera: ')
    priority = Column(Integer)
    source = Column(String(564), default='Customer ')
    risk = Column(String(15), default='High ')
    verifyMethod = Column(String(15), default='Method1 ')
    variability = Column(String(20))
    idRequirementStatus = Column(String(30), default='Status')
    dependencies = Column(String(55), default='R0X,R0X2')
    """dependencies = ('Benefit', secondary=assoc_req_dep, backref='requirement')"""
    idProductFeature = Column(String(20))
    idCompanyProject = Column(String(30), default='Company')
    idText = Column(String(255))
    idRequirementType = Column(String(3), default='FRQ')
    idComponent = Column(String(30), default='Component1')
    domain_id = Column(Integer, ForeignKey('domain.id'))
    domain = relationship("Domain")
    applicationEntitty_has_Requirement = Column(String(20))
    requirement_has_Actor = Column(String(20))
    requirement_has_ClassDiagram = Column(String(20))
    requirement_has_DomainRequirements = Column(String(20))
    requirement_has_EmailRequirements = Column(String(20))
    requirement_has_Requirement = Column(String(20))
    requirement_has_Requirement1 = Column(String(20))
    requirement_has_SubDomain = Column(String(20))
    requirementsTODO = Column(String(20))


    def __repr__(self):
        return self.name



"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
