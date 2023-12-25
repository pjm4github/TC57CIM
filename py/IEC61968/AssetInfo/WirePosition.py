from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetInfo.WirePhaseInfo import WirePhaseInfo
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Displacement import Displacement


class WirePosition(IdentifiedObject):
    """
    Implementation of the Class WirePosition
    Created on:      19-Dec-2023 11:44:16 AM

    Identification, spacing and configuration of the wires of a conductor with
    respect to a structure.
    """
    def __init__(self):
        super().__init__()
        # Signed horizontal distance from the wire at this position to a common reference
        # point.
        self.x_coord = Displacement()
        # Signed vertical distance from the wire at this position: above ground (positive
        # value) or burial depth below ground (negative value).
        self.y_coord = Displacement()
        self.wire_phase_info = WirePhaseInfo()

