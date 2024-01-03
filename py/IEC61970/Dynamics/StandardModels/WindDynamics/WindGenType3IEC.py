# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from typing import Any

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3IEC import WindTurbineType3IEC


class WindGenType3IEC(IdentifiedObject):

    """
    Parent class supporting relationships to IEC wind turbines Type 3 generator
    models of IEC type 3A and 3B.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.dipmax = PU()  # Maximum active current ramp rate (di_pmax)
        self.diqmax = PU()  # Maximum reactive current ramp rate (di_qmax)
        self.xs = PU()  # Electromagnetic transient reactance (x_S)
        self.wind_turbine_type3_iec = WindTurbineType3IEC()  # Wind turbine type 3 model with which this wind generator type 3 is associated.

