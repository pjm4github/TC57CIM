from IEC61968.Common.Status import Status  # Importing Status class from IEC61968.Common module
from IEC61970.Base.Core.IdentifiedObject import \
    IdentifiedObject  # Importing IdentifiedObject class from IEC61970.Base.Core module
from IEC62325.InfIEC62325.InfExternalInputs.ResourceGroupReq import ResourceGroupReq


class ResourceGroup(IdentifiedObject):
    """
    A logical grouping of resources that are used to model location of types of
    requirements for ancillary services such as spinning reserve zones, regulation
    zones, etc.
    @updated 03-Jan-2024 1:50:36 PM
    """

    def __init__(self):
        super().__init__()  # Calling the __init__() method of the superclass
        self.status = Status()  # Creating an instance of Status class and assigning it to the 'status' attribute
        self.type = ""  # Creating an instance of String class and assigning it to the 'type' attribute
        self.resource_group_reqs = ResourceGroupReq()
        # Creating an instance of ResourceGroupReq class and
        # assigning it to the 'resourceGroupReqs' attribute
