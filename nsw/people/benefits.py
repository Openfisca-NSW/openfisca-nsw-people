# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class is_family_tax_benefit_recipient(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "has been an FTB Recipient in the past year"


class is_full_age_pension_recipient(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Receives age pension from Department of Human Services"


class is_veterans_pension_recipient(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Receives full pension from Department of Veteran Affairs"
