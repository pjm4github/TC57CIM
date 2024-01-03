# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:28:11 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics.SynchronousMachineDynamics import \
    SynchronousMachineDynamics
from IEC61970.Dynamics.StandardModels.VoltageCompensatorDynamics.VCompIEEEType2 import VCompIEEEType2


class GenICompensationForGenJ(IdentifiedObject):
    """
    This class provides the resistive and reactive components of compensation for
    the generator associated with the IEEE Type 2 voltage compensator for current
    flow out of one of the other generators in the interconnection.
    """
    def __init__(self):
        super().__init__()
        self.rcij = PU()  # Resistive component of compensation of generator associated with this IEEE Type 2 voltage compensator for current flow out of another generator (Rcij).
        self.xcij = PU()  # Reactive component of compensation of generator associated with this IEEE Type 2 voltage compensator for current flow out of another generator (Xcij).
        self.VcompIEEEType2 = VCompIEEEType2()  # The standard IEEE Type 2 voltage compensator of this compensation.
        self.SynchronousMachineDynamics = SynchronousMachineDynamics()  # Standard synchronous machine out of which current flow is being compensated for.
