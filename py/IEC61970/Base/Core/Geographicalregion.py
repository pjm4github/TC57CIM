from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.SubGeographicalRegion import SubGeographicalRegion


class GeographicalRegion(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.regions = SubGeographicalRegion()  # All sub-geographical regions within this geographical region.
