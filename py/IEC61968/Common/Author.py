# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.ActivityRecord import ActivityRecord
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.DocumentPersonRole import DocumentPersonRole


class Author(DocumentPersonRole):
    
    def __init__(self):
        super().__init__()
        self.documents = Document()
        self.activity_records = ActivityRecord()
