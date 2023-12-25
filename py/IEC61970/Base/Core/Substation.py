# from equipment_container import EquipmentContainer
# from voltage_level import VoltageLevel
# from bay import Bay
# from dc_converter_unit import DCConverterUnit
# from feeder import Feeder
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Bay import Bay
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.EquipmentContainer import EquipmentContainer
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Feeder import Feeder
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.VoltageLevel import VoltageLevel
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC.DCConverterUnit import DCConverterUnit


class Substation(EquipmentContainer):
    def __init__(self):
        super().__init__()
        self.voltage_levels = VoltageLevel()  # The voltage levels within this substation.
        self.bays = [Bay()]  # Bays contained in the substation.
        self.dc_converter_unit = DCConverterUnit()  # The DC converter unit belonging to the substation.
        self.normal_energized_feeder = Feeder()  # The normal energized feeders of the substation. Also used for naming purposes.
