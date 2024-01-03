# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3or4IEC import WindTurbineType3or4IEC


class WindRefFrameRotIEC(IdentifiedObject):
    """
    Reference frame rotation model.

    Reference: IEC Standard 61400-27-1 Section 5.6.3.5.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:21 PM
    """

    def __init__(self) -> None:
        """
        Constructor for WindRefFrameRotIEC
        """
        super().__init__()
        self.tpll: Seconds = Seconds()  # Time constant for PLL first order filter model (T<sub>PLL</sub>).
        self.upll1: PU = PU()  # Voltage below which the angle of the voltage is filtered and possibly also frozen (u<sub>PLL1</sub>).
        self.upll2: PU = PU()  # Voltage (u<sub>PLL2</sub>) below which the angle of the voltage is frozen if u<sub>PLL2 <sub>is smaller or equal to u<sub>PLL1</sub>  . It is type dependent parameter.
        self.wind_turbine_type_3_or_4_iec: WindTurbineType3or4IEC = WindTurbineType3or4IEC()  # Wind turbine type 3 or 4 model with which this reference frame rotation model is associated.
