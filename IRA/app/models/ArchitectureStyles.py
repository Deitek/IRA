from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship



class ArchitectureStyles(Model):
    
    idArchitectureStyle = Column(Integer, primary_key=True)
    name = Column(String(150), unique = True, nullable=False)
    description = Column(String(564), default='Description: ')
    domainArchitecture_has_ApplicationType = Column(String(20))

    def __repr__(self):
        return self.name