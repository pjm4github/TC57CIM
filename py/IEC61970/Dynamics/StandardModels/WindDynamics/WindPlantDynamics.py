# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal import RemoteInputSignal
from IEC61970.Dynamics.StandardModels import DynamicsFunctionBlock
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics


class WindPlantDynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines Type 3 and 4 and wind
    plant IEC and user defined wind plants including their control models.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:21 PM
    """

    def __init__(self):
        super().__init__()
        self.wind_turbine_type3or4_dynamics = WindTurbineType3or4Dynamics()  # The wind turbine type 3 or 4
        # associated with this wind plant
        self.remote_input_signal = RemoteInputSignal()  # The remote signal with which this power plant is associated
