# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:41:50 2023
from IEC61970.Base.Domain.Reactance import Reactance
from IEC61970.Base.Wires.ShuntCompensator import ShuntCompensator


class Svc(ShuntCompensator):
    """
    SVC asset allows the capacitive and inductive ratings for each phase to be
    specified individually if required.
    @created 29-Dec-2023 5:59:41 PM
    """
    
    def __init__(self) -> None:
        super().__init__()
        """
        Maximum capacitive reactive power.
        """
        self.capacitive_rating = Reactance()

        """
        Maximum inductive reactive power.
        """
        self.inductive_rating = Reactance()
