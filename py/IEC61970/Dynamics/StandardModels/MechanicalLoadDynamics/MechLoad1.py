# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 16:59:22 2023
from IEC61970.Dynamics.StandardModels.MechanicalLoadDynamics.MechanicalLoadDynamics import MechanicalLoadDynamics


class MechLoad1(MechanicalLoadDynamics):
    """
    Mechanical load model type 1.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.a: float = 1.0  # Speed squared coefficient (a)
        self.b: float = 1.0  # Speed coefficient (b)
        self.d: float = 1.0  # Speed to the exponent coefficient (d)
        self.e: float = 1.0  # Exponent (e)
