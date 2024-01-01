# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:02:59 2023
# from IEC61970.Base.IdentifiedObject import IdentifiedObject
# from IEC61970.Base.Generation import GeneratingUnit
# from IEC61970.Base.Meas import AltGeneratingUnitMeas
from typing import Optional

from IEC61970.Base.ControlArea.AltGeneratingUnitMeas import AltGeneratingUnitMeas
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Generation.Production.GeneratingUnit import GeneratingUnit


class ControlAreaGeneratingUnit(IdentifiedObject):
    """
    A control area generating unit. This class is needed so that alternate control
    area definitions may include the same generating unit. Note only one instance
    within a control area should reference a specific generating unit.
    """
    def __init__(self) -> None:
        super().__init__()
        self.generating_unitOptional[GeneratingUnit] = GeneratingUnit()  # The generating unit specified for this control area. Note that a control area should include a GeneratingUnit only once.
        self.alt_generating_unit_measOptional[AltGeneratingUnitMeas] = AltGeneratingUnitMeas()  # The link to prioritized measurements for this GeneratingUnit.


