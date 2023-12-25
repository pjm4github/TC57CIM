# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:34:52 2023
from typing import Any, Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage


class EquivalentInjection(IdentifiedObject):
    """
    This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the point of connection.
    """

    def __init__(self) -> None:
        super().__init__()
        self.max_p: Optional[ActivePower] = ActivePower()  # Maximum active power of the injection.
        self.max_q: Optional[ReactivePower] = ReactivePower()  # Used for modeling of infeed for load flow exchange.
        self.min_p: Optional[ActivePower] = ActivePower()  # Minimum active power of the injection.
        self.min_q: Optional[ReactivePower] = ReactivePower()  # Used for modeling of infeed for load flow exchange.
        self.p: Optional[ActivePower] = ActivePower()  # Equivalent active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions.
        self.q: Optional[ReactivePower] = ReactivePower()  # Equivalent reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions.
        self.r: Optional[Resistance] = Resistance()  # Positive sequence resistance. Used to represent Extended-Ward (IEC 60909).
        self.r0: Optional[Resistance] = Resistance()  # Zero sequence resistance. Used to represent Extended-Ward (IEC 60909).
        self.r2: Optional[Resistance] = Resistance()  # Negative sequence resistance. Used to represent Extended-Ward (IEC 60909).
        self.regulation_capability: Optional[bool] = False  # Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage.
        self.regulation_status: Optional[bool] = False  # Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating.
        self.regulation_target: Optional[Voltage] = Voltage()  # The target voltage for voltage regulation.
        self.x: Optional[Reactance] = Reactance()  # Positive sequence reactance. Used to represent Extended-Ward (IEC 60909).
        self.x0: Optional[Reactance] = Reactance()  # Zero sequence reactance. Used to represent Extended-Ward (IEC 60909).
        self.x2: Optional[Reactance] = Reactance() #Negative sequence reactance. Used to represent Extended-Ward (IEC 60909).
