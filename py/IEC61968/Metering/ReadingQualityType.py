# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class ReadingQualityType(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.category = ""
        self.sub_category = ""
        self.system_id = ""
