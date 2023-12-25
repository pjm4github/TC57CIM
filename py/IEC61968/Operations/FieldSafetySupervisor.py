# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.CrewMember import CrewMember


class FieldSafetySupervisor(CrewMember):
    def __init__(self):
        super().__init__()
        self.released_safety_documents = None  # All safety documents released by this supervisor
        self.issued_safety_documents = None  # All safety documents issued to this supervisor
