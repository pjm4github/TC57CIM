# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.ISOUpperLayer import ISOUpperLayer
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.TCPAccessPoint import TCPAccessPoint


class PublicX509Certificate:
    """
    Used to convey information that will allow matching in order to determine which
    certificate to use.  Actual certificates are exchanged externally to the CIM
    exchange.
    @author: herb
    @version: 1.0
    @created: 15-Dec-2023 4:38:29 PM
    """

    def __init__(self) -> None:
        """
        Represents the CA that issued the certificate.  Defined to be per X.509.
        """
        self.issuer_name: Optional[str] = ""  #  Is the serial number of the certificate per X.509 definition.
        self.serial_number: Optional[str] = ""

        self.tcp_access_point: Optional[TCPAccessPoint] = TCPAccessPoint()
        self.iso_upper_layer: Optional[ISOUpperLayer] = ISOUpperLayer()
