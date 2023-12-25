# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Seconds import Seconds


class RecloseSequence(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.reclose_delay = Seconds()
        self.reclose_step = 0
