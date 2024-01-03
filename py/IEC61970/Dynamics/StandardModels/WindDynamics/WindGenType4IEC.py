# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType4aIEC import WindTurbineType4aIEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType4bIEC import WindTurbineType4bIEC
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class WindGenType4IEC(IdentifiedObject):
    """
    IEC Type 4 generator set model.

    Reference: IEC Standard 61400-27-1 Section 5.6.3.4.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:21 PM
    """
    from IEC61970.Base.Domain import PU, Seconds
    from IEC61970.Base.Core import IdentifiedObject

    def __init__(self):
        super().__init__()
        self.dipmax = PU()  # Maximum active current ramp rate (di_pmax)
        self.diqmax = PU()  # Maximum reactive current ramp rate (di_qmax)
        self.diqmin = PU()  # Minimum reactive current ramp rate (d_i_qmin)
        self.tg = Seconds()  # Time constant (T_g)
        self.wind_turbine_type4b_iec = WindTurbineType4bIEC()  # Wind turbine type 4B model with which this wind generator type 4
        self.wind_turbine_type4a_iec = WindTurbineType4aIEC()  # Wind turbine type 4A model with which this wind generator type 4
