# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class EndDeviceControlType(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.domain = ""
        self.event_or_action = ""
        self.sub_domain = ""
        self.type_ = ""
