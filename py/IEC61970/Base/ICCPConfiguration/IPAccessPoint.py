# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from datetime import datetime
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.IPAddressKind import IPAddressKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.SCADA.CommunicationLink import CommunicationLink


class IPAccessPoint(CommunicationLink):
    """
    @author SELAOST1
    @version 1.0
    @created 15-Dec-2023 4:38:27 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.address: Optional[str] = ""
        self.address_type: Optional[IPAddressKind] = IPAddressKind.IPv4
        self.gateway: Optional[str] = ""
        self.subnet: Optional[str] = ""

