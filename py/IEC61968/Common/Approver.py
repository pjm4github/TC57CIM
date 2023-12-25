# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.DocumentPersonRole import DocumentPersonRole


class Approver(DocumentPersonRole):
    def __init__(self):
        super().__init__()
        self.documents = Document()
