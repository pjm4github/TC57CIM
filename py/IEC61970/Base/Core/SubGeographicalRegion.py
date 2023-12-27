from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Core.Substation import Substation
from IEC61970.Base.Wires.Line import Line


class SubGeographicalRegion(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.lines = Line()  # The lines within the sub-geographical region.
        self.substations = Substation()  # The substations in this sub-geographical region.
