# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:35:24 2023
from datetime import datetime
from typing import Any, Optional

from openpyxl.pivot.table import Location

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Equipment import Equipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.PhaseCode import PhaseCode
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Faults.FaultCauseType import FaultCauseType
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Faults.FaultImpedance import FaultImpedance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Faults.PhaseConnectedFaultKind import PhaseConnectedFaultKind


class Fault(IdentifiedObject):
    """
    Abnormal condition causing current flow through conducting equipment, such as
    caused by equipment failure or short circuits from objects not typically
    modeled (for example, a tree falling on a line).
    @author T. Kostic
    @version 1.0
    @created 15-Dec-2023 4:38:27 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.impedance: Optional[FaultImpedance] = FaultImpedance()  # Fault impedance. Its usage is described by 'kind'.
        self.kind: Optional[PhaseConnectedFaultKind] = PhaseConnectedFaultKind.LINE_TO_GROUND  # The kind of phase fault.
        self.occurred_date_time: Optional[datetime] = datetime.now()  # The date and time at which the fault occurred.
        self.phases: Optional[PhaseCode] = PhaseCode.N  # The phases participating in the fault. The fault connections
                                           # into these phases are further specified by the type of fault.
        self.faulty_equipment: Optional[Equipment] = Equipment()  # Equipment carrying this fault.
        self.fault_cause_types: Optional[FaultCauseType] = FaultCauseType()  # All types of fault cause.
        self.location: Optional[Location] = Location()
