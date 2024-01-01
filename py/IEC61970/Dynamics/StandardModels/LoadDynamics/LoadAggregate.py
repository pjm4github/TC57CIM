# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 16:32:51 2023
from datetime import datetime
from typing import Any

from IEC61970.Dynamics.StandardModels.LoadDynamics.LoadDynamics import LoadDynamics


class LoadAggregate(LoadDynamics):
    """
    Standard aggregate load model comprised of static and/or dynamic components.
    A static load model represents the sensitivity of the real and reactive power
    consumed by the load to the amplitude and frequency of the bus voltage. A
    dynamic load model can used to represent the aggregate response of the motor
    components of the load.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        super().__init__()
