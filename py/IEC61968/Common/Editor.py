# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# editor.py
from IEC61968.Common.Document import Document
from IEC61968.Common.DocumentPersonRole import DocumentPersonRole


class Editor(DocumentPersonRole):
    def __init__(self):
        super().__init__()
        self.documents = Document()
