# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.TransmissionModeKind import TransmissionModeKind


class PanDisplay:
    def __init__(self):
        self.confirmation_required = False
        self.priority = ""
        self.text_message = ""
        self.transmission_mode = TransmissionModeKind()
