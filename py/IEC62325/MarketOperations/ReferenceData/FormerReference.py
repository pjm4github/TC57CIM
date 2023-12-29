# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class FormerReference(IdentifiedObject):
    """
    Used to indicate former references to the same piece of equipment. The ID,
    name, and effectivity dates are utilized.
    @created 28-Dec-2023 12:14:19 PM
    """

    def __init__(self):
        super().__init__()
