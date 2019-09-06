from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, BaseView, expose, has_access

"""from .models.models import Domain, Requirements"""
from .models import *

from . import appbuilder, db

class RequirementsModelView(ModelView):
    datamodel = SQLAInterface(Requirements)

    label_columns = {'Domain':'Domains'}
    list_columns = ['name', 'description', 'priority', 'dependencies', 'Domain']

    show_fieldsets = [
        (
            'Summary',
            {'fields': ['name', 'description', 'priority', 'Domain']}
        ),
        (
            'Requirements Info',
            {'fields': ['variability', 'type', 'dependencies'], 'expanded': False}
        ),
    ]

class DomainModelView(ModelView):
    datamodel = SQLAInterface(Domain)
    related_views = [RequirementsModelView]

class SubDomainModelView(ModelView):
    datamodel = SQLAInterface(SubDomain)

class RequirementsTODOModelView(ModelView):
    datamodel = SQLAInterface(RequirementsTODO)

class TextModelView(ModelView):
    datamodel = SQLAInterface(Text)

class CompanyProjectModelView(ModelView):
    datamodel = SQLAInterface(CompanyProject)

class ProductModelView(ModelView):
    datamodel = SQLAInterface(Product)

class ComponentModelView(ModelView):
    datamodel = SQLAInterface(Component)

class DomainArchitectureModelView(ModelView):
    datamodel = SQLAInterface(DomainArchitecture)

class ClassDiagramModelView(ModelView):
    datamodel = SQLAInterface(ClassDiagram)

class MinutesOfTheMeetingsModelView(ModelView):
    datamodel = SQLAInterface(MinutesOfMeetings)

class UseCaseModelView(ModelView):
    datamodel = SQLAInterface(UseCase)

class ProductFeaturesModelView(ModelView):
    datamodel = SQLAInterface(ProductFeatures)

class RequirementPrivilegesModelView(ModelView):
    datamodel = SQLAInterface(RequirementPrivileges)

class ArchitectureStyleModelView(ModelView):
    datamodel = SQLAInterface(ArchitectureStyles)

class ApplicationTypeModelView(ModelView):
    datamodel = SQLAInterface(ApplicationType)

class ActorModelView(ModelView):
    datamodel = SQLAInterface(Actor)

class CaseStoryModelView(ModelView):
    datamodel = SQLAInterface(CaseStory)

class AttendeesModelView(ModelView):
    datamodel = SQLAInterface(Attendees)

class ContextModelView(ModelView):
    datamodel = SQLAInterface(Context)

class ClassModelView(ModelView):
    datamodel = SQLAInterface(Class)

class EmailRequirementsModelView(ModelView):
    datamodel = SQLAInterface(EmailRequirements)

class DomainRequirementsModelView(ModelView):
    datamodel = SQLAInterface(DomainRequirements)

class DomainEntityActionModelView(ModelView):
    datamodel = SQLAInterface(DomainEntityAction)

class DomainEntityAttributesModelView(ModelView):
    datamodel = SQLAInterface(DomainEntityAttributes)

class DomainEntityModelView(ModelView):
    datamodel = SQLAInterface(DomainEntity)

class RequirementStatusModelView(ModelView):
    datamodel = SQLAInterface(RequirementStatus)

class RequirementTypeModelView(ModelView):
    datamodel = SQLAInterface(RequirementType)

class RequirementRolesModelView(ModelView):
    datamodel = SQLAInterface(RequirementRoles)

class ActionItemsModelView(ModelView):
    datamodel = SQLAInterface(ActionItems)

"""Menus for Input Options"""
appbuilder.add_view(ProductModelView, "Product", category='General')
appbuilder.add_view(ProductFeaturesModelView, "Product Features", category='General')
appbuilder.add_view(CompanyProjectModelView, "Company Project", category='General')

"""Menus for Input Options"""
appbuilder.add_view(TextModelView, "Text", category='Input')
appbuilder.add_view(EmailRequirementsModelView, "Email Requirements", category='Input')

"""Menus for Domains and Applications"""
appbuilder.add_view(DomainEntityModelView, "Domain Entities", category='Domain/App')
appbuilder.add_view(DomainEntityActionModelView, "Domain Entity Actions", category='Domain/App')
appbuilder.add_view(DomainEntityAttributesModelView, "Domain Entity Attributes", category='Domain/App')

"""Menus for Requirements Options"""
appbuilder.add_view(RequirementsModelView, "Requirement", category='Requirements')
appbuilder.add_view(ActorModelView, "Requirement Actors", category='Requirements')
appbuilder.add_view(DomainModelView, "Domain", category='Requirements')
appbuilder.add_view(SubDomainModelView, "SubDomain", category='Requirements')
"""appbuilder.add_link("Manage", href='/requirements/subdomain/manage', category='Requirements')"""
appbuilder.add_view(RequirementsTODOModelView, "RequirementsTODO", category='Requirements')

appbuilder.add_view(RequirementPrivilegesModelView, "Requirement Privileges", category='Requirements')
appbuilder.add_view(DomainRequirementsModelView, "Domain Requirements", category='Requirements')
appbuilder.add_view(RequirementStatusModelView, "Requirement Status", category='Requirements')
appbuilder.add_view(RequirementTypeModelView, "Requirement Types", category='Requirements')
appbuilder.add_view(RequirementRolesModelView, "Requirement Roles", category='Requirements')



"""Menus for Analysis Options"""
appbuilder.add_view(UseCaseModelView, "Use Cases", category='Analysis')
appbuilder.add_view(CaseStoryModelView, "Case Stories", category='Analysis')



"""Menus for Design Options"""
appbuilder.add_view(ComponentModelView, "Component", category='Design')
appbuilder.add_view(ArchitectureStyleModelView, "Architecture Style", category='Design')
appbuilder.add_view(ApplicationTypeModelView, "Application Type", category='Design')
appbuilder.add_view(DomainArchitectureModelView, "Domain Architecture", category='Design')
appbuilder.add_view(ClassDiagramModelView, "Class Diagram", category='Design')
"""
appbuilder.add_view(ClassModelView, "Class", category='Design')
appbuilder.add_view(ContextModelView, "Context", category='Design')
"""
appbuilder.add_view(MinutesOfTheMeetingsModelView, "Minutes of the Meetings", category='Output')
appbuilder.add_view(AttendeesModelView, "Meeting Attendees", category='Output')
appbuilder.add_view(ActionItemsModelView, "Meeting Action Items", category='Output')







"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
