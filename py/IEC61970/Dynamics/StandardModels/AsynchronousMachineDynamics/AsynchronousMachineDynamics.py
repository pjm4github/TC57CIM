# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:57:45 2023
from IEC61970.Base.Wires.AsynchronousMachine import AsynchronousMachine
from IEC61970.Dynamics.StandardModels.RotatingMachineDynamics import RotatingMachineDynamics


class AsynchronousMachineDynamics(RotatingMachineDynamics):
    """ 
    Asynchronous machine whose behaviour is described by reference to a standard
    model expressed in either time constant reactance form or equivalent circuit form
    or by definition of a user-defined model.
    
    Parameter Notes:
    - Asynchronous machine parameters such as Xl, Xs etc. are actually
        used as inductances (L) in the model, but are commonly referred to as
        reactances since, at nominal frequency,
        the per-unit values are the same.
    - However, some references use the symbol L instead of X.
    
    @author: tsaxton
    @version: 1.0
    @created: 29-Dec-2023 11:24:17 PM
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.asynchronous_machine: AsynchronousMachine = AsynchronousMachine()


