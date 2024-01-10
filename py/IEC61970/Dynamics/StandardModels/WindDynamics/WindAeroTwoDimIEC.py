# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.AngleDegrees import AngleDegrees
from IEC61970.Base.Domain.PU import PU
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3IEC import WindTurbineType3IEC


class WindAeroTwoDimIEC(IdentifiedObject):
    """
    Two-dimensional aerodynamic model.

    Reference: IEC Standard 614000-27-1 Section 5.6.1.3.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.dp_omega: PU = PU()
        # Partial derivative of aerodynamic power with respect to changes in WTR speed      (dp<sub>omega</sub>). It is type dependent parameter.

        self.dp_theta: PU = PU()
        # Partial derivative of aerodynamic power with respect to changes in pitch angle        (dp<sub>theta</sub>). It is type dependent parameter.

        self.dp_v1: PU = PU()
        # Partial derivative (dp<sub>v1</sub>). It is type dependent parameter.

        self.omega_zero: PU = PU()
        # Rotor speed if the wind turbine is not derated (omega<sub>0</sub>). It is type dependent parameter.

        self.p_avail: PU = PU()
        # Available aerodynamic power (p<sub>avail</sub>). It is case dependent        parameter.

        self.theta_v2: Optional[AngleDegrees] = AngleDegrees()
        # Blade angle at twice rated wind speed (theta<sub>v2</sub>). It is         type dependent parameter.

        self.theta_zero: Optional[AngleDegrees] = AngleDegrees()
        # Pitch angle if the wind turbine is not derated        (theta<sub>0</sub>). It is case dependent parameter.

        self.wind_turbine_type3_iec: Optional[WindTurbineType3IEC] = WindTurbineType3IEC()
        # Wind turbine type 3 model with which this wind aerodynamic model is associated.

