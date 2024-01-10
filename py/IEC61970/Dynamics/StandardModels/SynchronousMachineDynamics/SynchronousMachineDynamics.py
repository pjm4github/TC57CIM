# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:07:00 2023
from IEC61970.Base.Wires.SynchronousMachine import SynchronousMachine
from IEC61970.Dynamics.StandardModels.RotatingMachineDynamics import RotatingMachineDynamics
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class SynchronousMachineDynamics(RotatingMachineDynamics):
    """
    Synchronous machine whose behaviour is described by reference to a standard model expressed in one of the following
    forms:
    - simplified (or classical), where a group of generators or motors is not modelled in detail
    - detailed, in equivalent circuit form
    - detailed, in time constant reactance form
    - or by definition of a user-defined model.

    Note: It is a common practice to represent small generators by a negative load rather than by a dynamic generator
    model when performing dynamics simulations. In this case a SynchronousMachine in the static model is not
    represented by anything in the dynamics model, instead it is treated as ordinary load.

    Parameter Notes:
    Synchronous machine parameters such as Xl, Xd, Xp etc. are actually used as inductances (L) in the models, but are
    commonly referred to as reactances since, at nominal frequency, the per unit values are the same. However,
    some references use the symbol L instead of X.
    """

    def __init__(self) -> None:
        super().__init__()
        self.synchronous_machine: SynchronousMachine = SynchronousMachine()  # Synchronous machine to which synchronous machine dynamics model applies
        self.turbine_governor_dynamics: TurbineGovernorDynamics = TurbineGovernorDynamics()  # Turbine-governor model associated with this synchronous machine model
