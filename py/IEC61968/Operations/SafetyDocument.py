from IEC61968.Common.Document import Document
from IEC61970.Base.Domain.DateTime import DateTime


class SafetyDocument(Document):
    def __init__(self):
        super().__init__()
        self.issued_date_time = DateTime()  # Date and time this safety document has been issued.
        self.released_date_time = DateTime()  # Date and time this safety document has been released.
