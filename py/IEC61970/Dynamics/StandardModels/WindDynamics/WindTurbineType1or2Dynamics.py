# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal import RemoteInputSignal
from IEC61970.Dynamics.StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics import \
    AsynchronousMachineDynamics
from IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock


class WindTurbineType1or2Dynamics(DynamicsFunctionBlock):
    """ 
    Parent class supporting relationships to wind turbines Type 1 and 2 and their
    control models.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:21 PM
    """

    def __init__(self) -> None:
        """
        Asynchronous machine model with which this wind generator type 1 or 2 model is 
        associated.
        """
        super().__init__()
        self.asynchronous_machine_dynamics: AsynchronousMachineDynamics = AsynchronousMachineDynamics()

        """
        Remote input signal used by this wind generator Type 1 or Type 2 model.
        """
        self.remote_input_signal: RemoteInputSignal = RemoteInputSignal()
