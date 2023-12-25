# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
# from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.TCPAccessPoint import TCPAccessPoint
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.TCPAccessPoint import TCPAccessPoint


class ISOUpperLayer(TCPAccessPoint):

    def __init__(self) -> None:
        super().__init__()
        self.ae_invoke: int = 0
        self.ae_qual: int = 0
        self.ap_invoke: int = 0
        self.ap_title: str = ""
        self.osi_psel: str = ""
        self.osi_ssel: str = ""
        self.osi_tsel: str = ""

