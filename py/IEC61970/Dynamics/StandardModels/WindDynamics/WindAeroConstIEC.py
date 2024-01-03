# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Dynamics.StandardModels.WindDynamics.WindGenTurbineType1aIEC import WindGenTurbineType1aIEC


class WindAeroConstIEC(IdentifiedObject):
    """
    The constant aerodynamic torque model assumes that the aerodynamic torque is
    constant.

    Reference: IEC Standard 61400-27-1 Section 5.6.1.1.
    """
    def __init__(self) -> None:
        super().__init__()
        # Wind turbine type 1A model with which this wind aerodynamic model is associated.
        self.wind_gen_turbine_type_1a_iec: WindGenTurbineType1aIEC = WindGenTurbineType1aIEC()
