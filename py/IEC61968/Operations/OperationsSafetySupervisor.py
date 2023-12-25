# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Operator import Operator


class OperationsSafetySupervisor(Operator):
    """
    Operator with responsibility that the work in high voltage installation is
    executed in a safe manner and according to safety regulation.
    """

    def __init__(self):
        super().__init__()
        self.released_safety_documents = Document()  # All safety documents released to this supervisor
        self.issued_safety_documents = Document()  # All safety documents issued by this supervisor
