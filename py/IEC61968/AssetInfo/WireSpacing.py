# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetInfo.WirePosition import WirePosition
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetInfo.WireUsageKind import WireUsageKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.DuctBank import DuctBank
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.Structure import Structure
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Length import Length


class WireSpacing(IdentifiedObject):
    """
    Wire spacing data that associates multiple wire positions with the line segment,
    and allows to calculate line segment impedances. Number of phases can be
    derived from the number of associated wire positions whose phase is not neutral.

    @author T. Kostic
    @version 1.0
    @created 18-Dec-2023 10:14:01 PM

    """

    def __init__(self):
        super().__init__()
        self.is_cable = True
        self.phase_wire_count = 0
        self.phase_wire_spacing = Length()
        self.usage = WireUsageKind()
        self.wire_positions = WirePosition()
        self.structures = Structure()
        self.duct_bank = DuctBank()
