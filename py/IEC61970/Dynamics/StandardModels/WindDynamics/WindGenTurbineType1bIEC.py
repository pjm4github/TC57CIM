# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Dynamics.StandardModels.WindDynamics.WindPitchContPowerIEC import WindPitchContPowerIEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType1or2IEC import WindTurbineType1or2IEC


class WindGenTurbineType1bIEC(WindTurbineType1or2IEC):
    """
    Wind turbine IEC Type 1B.

    Reference: IEC Standard 61400-27-1, section 5.5.2.3.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.wind_pitch_cont_power_iec: WindPitchContPowerIEC = WindPitchContPowerIEC()
