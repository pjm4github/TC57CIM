# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from typing import Any

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3or4IEC import WindTurbineType3or4IEC


class WindContQlimIEC(IdentifiedObject):
    """
    Constant Q limitation model.

    Reference: IEC Standard 61400-27-1 Section 5.6.5.9.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    def __init__(self) -> None:
        # Constructor
        super().__init__()
        self.q_max: PU = PU()  # Maximum reactive power (q_max). It is type dependent parameter.
        self.q_min: PU = PU()  # Minimum reactive power (q_min). It is type dependent parameter.
        self.wind_turbine_type_3or4_iec: WindTurbineType3or4IEC = WindTurbineType3or4IEC()  # Wind generator type 3 or 4 model with which this constant Q limitation model        is associated.
