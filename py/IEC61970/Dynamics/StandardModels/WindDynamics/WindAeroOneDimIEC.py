# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3IEC import WindTurbineType3IEC


class WindAeroOneDimIEC(IdentifiedObject):
    """
    One-dimensional aerodynamic model.
    Reference: IEC Standard 614000-27-1 Section 5.6.1.2.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """
    def __init__(self) -> None:
        # WindAeroOneDimIEC constructor
        super().__init__()
        self.ka: float = 1.0  # Aerodynamic gain (ka). It is type dependent parameter.
        self.theta_omega: float = 1.0  # Initial pitch angle (theta_omega). It is case dependent parameter.
        self.wind_turbine_type3_iec: WindTurbineType3IEC = WindTurbineType3IEC()  # Wind turbine type 3 model with which this wind aerodynamic model is associated.
