# AssetFunction.py
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class AssetFunction(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.config_id = ""
        self.firmware_id = ""
        self.hardware_id = ""
        self.password = ""
        self.program_id = ""
