from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class Context(Model):
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return self.name