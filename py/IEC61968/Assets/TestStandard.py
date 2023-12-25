# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.ASTMStandard import ASTMStandard
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.CIGREStandard import CIGREStandard
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.DINStandard import DINStandard
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.DobleStandard import DobleStandard
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.EPAStandard import EPAStandard
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.IECStandard import IECStandard
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.IEEEStandard import IEEEStandard
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.ISOStandard import ISOStandard
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.LaborelecStandard import LaborelecStandard
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.TAPPIStandard import TAPPIStandard
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.TestMethod import TestMethod
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.TestVariantKind import TestVariantKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.UKMinistryOfDefenceStandard import UKMinistryOfDefenceStandard
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.WEPStandard import WEPStandard
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class TestStandard(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.test_method = TestMethod.D1275A
        self.test_standard_astm = ASTMStandard()
        self.test_standard_cigre = CIGREStandard()
        self.test_standard_din = DINStandard()
        self.test_standard_doble = DobleStandard()
        self.test_standard_epa = EPAStandard()
        self.test_standard_iec = IECStandard()
        self.test_standard_ieee = IEEEStandard()
        self.test_standard_iso = ISOStandard()
        self.test_standard_laborelec = LaborelecStandard()
        self.test_standard_tappi = TAPPIStandard()
        self.test_standard_uk_ministry_of_defence = UKMinistryOfDefenceStandard()
        self.test_standard_wep = WEPStandard()
        self.test_variant = TestVariantKind.TESTING_DONE_AT_TEMPERATURE_OF_0_C
