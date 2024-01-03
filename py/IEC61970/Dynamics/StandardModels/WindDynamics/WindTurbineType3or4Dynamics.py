# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from typing import Any

from IEC61970.Base.Wires.PowerElectronicsConnection import PowerElectronicsConnection
from IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal import RemoteInputSignal
from IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock


class WindTurbineType3or4Dynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines Type 3 and 4 and wind
    plant including their control models.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:21 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.remote_input_signal: RemoteInputSignal = RemoteInputSignal()
        self.power_electronics_connection: PowerElectronicsConnection = PowerElectronicsConnection()

