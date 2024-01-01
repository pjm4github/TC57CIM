# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:34:52 2023
from typing import Any, Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.Reactance import Reactance
from IEC61970.Base.Domain.ReactivePower import ReactivePower
from IEC61970.Base.Domain.Resistance import Resistance
from IEC61970.Base.Domain.Voltage import Voltage


class EquivalentInjection(IdentifiedObject):
    """
    This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the point of connection.
    """

    def __init__(self) -> None:
        super().__init__()
        self.max_pOptional[ActivePower] = ActivePower()  # Maximum active power of the injection.
        self.max_qOptional[ReactivePower] = ReactivePower()  # Used for modeling of infeed for load flow exchange.
        self.min_pOptional[ActivePower] = ActivePower()  # Minimum active power of the injection.
        self.min_qOptional[ReactivePower] = ReactivePower()  # Used for modeling of infeed for load flow exchange.
        self.pOptional[ActivePower] = ActivePower()  # Equivalent active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions.
        self.qOptional[ReactivePower] = ReactivePower()  # Equivalent reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions.
        self.rOptional[Resistance] = Resistance()  # Positive sequence resistance. Used to represent Extended-Ward (IEC 60909).
        self.r0Optional[Resistance] = Resistance()  # Zero sequence resistance. Used to represent Extended-Ward (IEC 60909).
        self.r2Optional[Resistance] = Resistance()  # Negative sequence resistance. Used to represent Extended-Ward (IEC 60909).
        self.regulation_capabilityOptional[bool] = False  # Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage.
        self.regulation_statusOptional[bool] = False  # Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating.
        self.regulation_targetOptional[Voltage] = Voltage()  # The target voltage for voltage regulation.
        self.xOptional[Reactance] = Reactance()  # Positive sequence reactance. Used to represent Extended-Ward (IEC 60909).
        self.x0Optional[Reactance] = Reactance()  # Zero sequence reactance. Used to represent Extended-Ward (IEC 60909).
        self.x2Optional[Reactance] = Reactance() #Negative sequence reactance. Used to represent Extended-Ward (IEC 60909).
