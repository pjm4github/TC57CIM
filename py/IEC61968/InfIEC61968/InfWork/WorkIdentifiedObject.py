# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class WorkIdentifiedObject(IdentifiedObject):
    """
    Shadow class for IdentifiedObject, to isolate subclassing from this package. If
    any subclass gets normative and needs inheritance, it will inherit directly
    from IdentifiedObject.
    """

    def __init__(self) -> None:
        super().__init__()