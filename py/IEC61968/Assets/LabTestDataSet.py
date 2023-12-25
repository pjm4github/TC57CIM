# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.AssetTestLab import AssetTestLab
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.ProcedureDataSet import ProcedureDataSet
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.Specimen import Specimen
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.TestReason import TestReason

class LabTestDataSet(ProcedureDataSet):
    
    def __init__(self):
        super().__init__()
        self.conclusion = ""
        self.conclusion_confidence = ""
        self.reason_for_test = TestReason()
        self.test_equipment_id = ""
        self.specimen = Specimen()
        self.asset_test_lab = AssetTestLab()
