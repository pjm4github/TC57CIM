# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.IPAccessPoint import IPAccessPoint


class TCPAccessPoint(IPAccessPoint):

    def __init__(self) -> None:
        super().__init__()
        self.keep_alive_time: Optional[int] = 0
        self.port: Optional[int] = 0
