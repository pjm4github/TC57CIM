# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023


from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType1or2IEC import WindTurbineType1or2IEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3IEC import WindTurbineType3IEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType4bIEC import WindTurbineType4bIEC


class WindMechIEC(IdentifiedObject):
    """
    Two mass model.

    Reference: IEC Standard 61400-27-1 Section 5.6.2.1.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:21 PM
    """

    def __init__(self) -> None:
        """Constructor"""
        super().__init__()
        self.cdrt: PU = PU()  # Drive train damping (cdrt). It is type dependent parameter.
        self.hgen: Seconds = Seconds()  # Inertia constant of generator (H_gen). It is type dependent parameter.
        self.hwtr: Seconds = Seconds()  # Inertia constant of wind turbine rotor (H_WTR). It is type dependent parameter.
        self.kdrt: PU = PU()  # Drive train stiffness (k_drt). It is type dependent parameter.
        self.wind_turbine_type_4b_iec: WindTurbineType4bIEC = WindTurbineType4bIEC()  # Wind turbine type 4B model with which this wind mechanical model is associated.
        self.wind_turbine_type_3_iec: WindTurbineType3IEC = WindTurbineType3IEC()  # Wind turbine Type 3 model with which this wind mechanical model is associated.
        self.wind_turbine_type_1or2_iec: WindTurbineType1or2IEC = WindTurbineType1or2IEC()  # Wind generator type 1 or 2 model with which this wind mechanical model is associated.
