from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class DataSetMember:
    """
    A generic description of a version of instance data.
    Author: 222206
    Version: 1.0
    Created: 22-Dec-2023 4:59:45 PM
    """
    def __init__(self):
        self.mrid = str()  # Master resource identifier, unique within an exchange context
        self.properties_object = IdentifiedObject()  # Placeholder for the CIM object holding properties (IdentifiedObject)
        self.target_object = IdentifiedObject()  # Placeholder for the registered CIM object (IdentifiedObject)
        # Assuming IdentifiedObject is a previously defined class
        # If IdentifiedObject is not defined, this will raise an error and needs to be implemented
