from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.api import ModelRestApi

from .import appbuilder
"""from .models.models import Requirements, Domain"""
from .models import *


"""
def fill_gender():
    try:
        db.session.add(Gender(name="Male"))
        db.session.add(Gender(name="Female"))
        db.session.commit()
    except Exception:
        db.session.rollback()


db.create_all()
fill_gender()
"""

class RequirementsModelApi(ModelRestApi):
    resource_name = 'requirement'
    datamodel = SQLAInterface(Requirements)
    allow_browser_login = True

appbuilder.add_api(RequirementsModelApi)



class DomainModelApi(ModelRestApi):
    resource_name = "domain"
    datamodel = SQLAInterface(Domain)
    allow_browser_login = True

appbuilder.add_api(DomainModelApi)