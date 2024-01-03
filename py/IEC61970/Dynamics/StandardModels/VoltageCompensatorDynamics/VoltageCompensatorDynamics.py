# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:28:11 2023
from IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal import RemoteInputSignal
from IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class VoltageCompensatorDynamics(DynamicsFunctionBlock):
    """
    Voltage compensator function block whose behaviour is described by reference to
    a standard model or by definition of a user-defined model.
    @author: tsaxton
    @version: 1.0
    @created: 29-Dec-2023 11:24:20 PM
    """
    def __init__(self):
        super().__init__()
        self.excitation_system_dynamics = ExcitationSystemDynamics()  # Excitation system model with which this voltage compensator is associated.
        self.remote_input_signal = RemoteInputSignal()  # Remote input signal used by this voltage compensator model.
