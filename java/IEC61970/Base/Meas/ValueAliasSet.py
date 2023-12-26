#######################################################
# 
# ValueAliasSet.py
# Python implementation of the Class ValueAliasSet
# Generated by Enterprise Architect
# Created on:      25-Dec-2023 8:32:04 PM
# 
#######################################################
from IEC61970.Base.Meas.ValueToAlias import ValueToAlias
from IEC61970.Base.Meas.Discrete import Discrete
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject

class ValueAliasSet(IdentifiedObject):
    """Describes the translation of a set of values into a name and is intendend to
    facilitate cusom translations. Each ValueAliasSet has a name, description etc.
    A specific Measurement may represent a discrete state like Open, Closed,
    Intermediate etc. This requires a translation from the MeasurementValue.value
    number to a string, e.g. 0->"Invalid", 1->"Open", 2->"Closed", 3-
    >"Intermediate". Each ValueToAlias member in ValueAliasSet.Value describe a
    mapping for one particular value to a name.
    """
    # The ValueToAlias mappings included in the set.
    Values= ValueToAlias()

    # The Measurements using the set for translation.
    Discretes= Discrete()