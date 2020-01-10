# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Family
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class age_in_months(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Person's age (in months)"

    # A person's age is computed according to its birth date.
    def formula(persons, period, parameters):
        is_birthday_past = persons('is_birthday_past', period)
        age_in_years = persons('age', period) + where(is_birthday_past, 0, 1)
        birth_month = persons('birth_month', period)
        return (age_in_years * 12) + (period.start.month - birth_month)


class is_birthday_past(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH

    def formula(persons, period, parameters):
        birth = persons('birth', period)
        birth_month = persons('birth_month', period)
        birth_day = (birth - birth.astype('datetime64[M]') + 1).astype(int)
        return (birth_month < period.start.month) + (birth_month == period.start.month) * (birth_day <= period.start.day)


class birth_month(Variable):
    value_type = int
    entity = Person
    definition_period = ETERNITY  # This variable cannot change over time.

    def formula(persons, period, parameters):
        return persons('birth', period).astype('datetime64[M]').astype(int) % 12 + 1
