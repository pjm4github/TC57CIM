# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


# A constraint term is one element of a linear constraint.
class ConstraintTerm(IdentifiedObject):

    def __init__(self) -> None:
        super().__init__()
        # 	 * The function is an enumerated value that can be 'active', 'reactive', or 'VA'
        # 	 * to indicate the type of flow.
        self.factor: str = ""
        self.function: str = ""
