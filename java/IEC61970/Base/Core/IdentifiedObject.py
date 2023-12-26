#######################################################
# 
# IdentifiedObject.py
# Python implementation of the Class IdentifiedObject
# Generated by Enterprise Architect
# Created on:      25-Dec-2023 8:31:59 PM
# 
#######################################################
from IEC61970.Base.Domain.String import String
from IEC61970.Base.DiagramLayout.DiagramObject import DiagramObject

class IdentifiedObject:
    """This is a root class to provide common identification for all classes needing
    identification and naming attributes.
    """
    # The diagram objects that are associated with the domain object.
    DiagramObjects= DiagramObject()
