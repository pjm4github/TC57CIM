# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Dynamics.StandardModels.WindDynamics.WindPlantDynamics import WindPlantDynamics
from IEC61970.Dynamics.StandardModels.WindDynamics.WindPlantReactiveControlIEC import WindPlantReactiveControlIEC


class WindPlantIEC(WindPlantDynamics):
    """
    Simplified IEC type plant level model.
    Reference: IEC 61400-27-1, Annex D.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:21 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.wind_plant_reactive_control_iec: WindPlantReactiveControlIEC = WindPlantReactiveControlIEC() # Wind plant model with which this wind reactive control is associated.
