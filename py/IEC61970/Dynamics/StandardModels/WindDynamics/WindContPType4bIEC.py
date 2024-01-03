# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType4bIEC import WindTurbineType4bIEC


class WindContPType4bIEC(IdentifiedObject):
    """
    P control model Type 4B.

    Reference: IEC Standard 61400-27-1 Section 5.6.5.6.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """
    def __init__(self):
        super().__init__()
        self.dp_maxp4b = PU()  # Maximum wind turbine power ramp rate (dp_maxp4B)
        self.t_paero = Seconds()  # Time constant in aerodynamic power response (T_paero)
        self.t_pordp4b = Seconds()  # Time constant in power order lag (T_pordp4B)
        self.t_ufiltp4b = Seconds()  # Voltage measurement filter time constant (T_ufiltp4B)
        # Wind turbine type 4B model with which this wind control P type 4B model is associated.
        self.wind_turbine_type4b_iec = WindTurbineType4bIEC()
