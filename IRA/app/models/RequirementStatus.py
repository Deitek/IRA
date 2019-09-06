from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class RequirementStatus(Model):
    
    idRequirementStatus = Column(Integer, primary_key=True)
    name = Column(String(150), unique = True, nullable=False)
    requirements_id = Column(Integer, ForeignKey('requirements.id'))
    requirement = relationship("Requirements")
        
    def __repr__(self):
        return self.name