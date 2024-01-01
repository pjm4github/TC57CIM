# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal import RemoteInputSignal
from IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class PowerSystemStabilizerDynamics(DynamicsFunctionBlock):
    """
    Power system stabilizer function block whose behaviour is described by reference to a standard model
    or by definition of a user-defined model.
    @author: tsaxton
    @version: 1.0
    @created: 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        """
        Excitation system model with which this power system stabilizer model is associated.
        """
        super().__init__()
        self.excitation_system_dynamics: ExcitationSystemDynamics = ExcitationSystemDynamics()


        """
        Remote input signal used by this power system stabilizer model.
        """
        self.remote_input_signal: RemoteInputSignal = RemoteInputSignal()


