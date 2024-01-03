# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from pydantic import BaseModel
from datetime import datetime

from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindGenType3IEC import WindGenType3IEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType4IEC import WindTurbineType4IEC


class WindGenType3aIEC(WindGenType3IEC):
    """
    IEC Type 3A generator set model.

    Reference: IEC Standard 61400-27-1 Section 5.6.3.2.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    def __init__(self):
        super().__init__()
        self.kpc = 0.0  # Current PI controller proportional gain (K_Pc)
        self.tic = Seconds()  # Current PI controller integration time constant (T_Ic)
        self.wind_turbine_type4_iec = WindTurbineType4IEC()  # Wind turbine type 4 model with which this wind generator type 3A model is associated
