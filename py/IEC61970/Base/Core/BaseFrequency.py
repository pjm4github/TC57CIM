# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:03:56 2023


from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Frequency import Frequency


class BaseFrequency(IdentifiedObject):
    """
    The class describe a base frequency for a power system network. In case of
    multiple power networks with different frequencies, e.g. 50 or 60 Hertz each
    network will have its own base frequency class hence it is assumed that power
    system objects having different base frequencies appear in separate documents
    where each document has a single base frequency instance.
    """

    def __init__(self) -> None:
        super().__init__()
        self.frequency = Frequency()

