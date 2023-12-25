
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.ComDirectionKind import ComDirectionKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.ComTechnologyKind import ComTechnologyKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceFunction import EndDeviceFunction


class ComFunction(EndDeviceFunction):
    # #  * Communication function of communication equipment or a device such as a meter.
    # #  * @created 20-Dec-2023 6:23:27 PM
    def __init__(self):
        super().__init__()
        self.amr_address = ""  # Communication ID number (e.g. serial number, IP address, telephone number, etc.) of the AMR module which serves this meter.
        self.amr_router = ""  # Communication ID number (e.g. port number, serial number, data collector ID, etc.) of the parent device associated to this AMR module.
        self.direction = ComDirectionKind.BI_DIRECTIONAL  # Kind of communication direction.
        self.technology = ComTechnologyKind.RF  # Kind of communication technology.
