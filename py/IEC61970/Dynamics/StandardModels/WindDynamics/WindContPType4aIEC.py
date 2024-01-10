# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType4aIEC import WindTurbineType4aIEC


class WindContPType4aIEC(IdentifiedObject):
    """
    P control model Type 4A.

    Reference: IEC Standard 61400-27-1 Section 5.6.5.5.
    """

    def __init__(self):
        super().__init__()
        # Maximum wind turbine power ramp rate (dp_max_p4a). It is project dependent parameter.
        self.dp_max_p4a = PU()  # Typical value: None

        # Time constant in power order lag (t_pord_p4a). It is type dependent parameter.
        self.t_pord_p4a = Seconds()  # Typical value: None

        # Voltage measurement filter time constant (t_u_filt_p4a). It is type dependent parameter.
        self.t_u_filt_p4a = Seconds()  # Typical value: None

        # Wind turbine type 4A model with which this wind control P type 4A model is associated.
        self.wind_turbine_type_4a_iec = WindTurbineType4aIEC()
