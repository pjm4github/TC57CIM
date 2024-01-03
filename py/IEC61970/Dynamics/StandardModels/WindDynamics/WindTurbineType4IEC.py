# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3or4IEC import WindTurbineType3or4IEC


class WindTurbineType4IEC(WindTurbineType3or4IEC):
    """
    Parent class supporting relationships to IEC wind turbines Type 4 including
    their control models.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:21 PM
    """
    def __init__(self) -> None:
        super().__init__()
