# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.AngleDegrees import AngleDegrees
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3IEC import WindTurbineType3IEC


class WindContPitchAngleIEC(IdentifiedObject):
    """
    Pitch angle control model.

    Reference: IEC Standard 61400-27-1 Section 5.6.5.2.
    """
    def __init__(self):
        super().__init__()
        self.dthetamax = 0.0  # Maximum pitch positive ramp rate (theta_max). It is type dependent parameter. Unit = degrees/sec.
        self.dthetamin = 0.0  # Maximum pitch negative ramp rate (theta_min). It is type dependent parameter. Unit = degrees/sec.
        self.kic = PU()  # Power PI controller integration gain (K_Ic). It is type dependent parameter.
        self.kiomega = PU()  # Speed PI controller integration gain (K_Iomega). It is type dependent parameter.
        self.kpc = PU()  # Power PI controller proportional gain (K_Pc). It is type dependent parameter.
        self.kpomega = PU()  # Speed PI controller proportional gain (K_Pomega). It is type dependent parameter.
        self.kpx = PU()  # Pitch cross coupling gain (K_PX). It is type dependent parameter.
        self.thetamax = AngleDegrees()  # Maximum pitch angle (theta_max). It is type dependent parameter.
        self.thetamin = AngleDegrees()  # Minimum pitch angle (theta_min). It is type dependent parameter.
        self.ttheta = Seconds()  # Pitch time constant (t_theta). It is type dependent parameter.
        self.wind_turbine_type_3iec = WindTurbineType3IEC()  # Wind turbine type 3 model with which this pitch control model is associated.
