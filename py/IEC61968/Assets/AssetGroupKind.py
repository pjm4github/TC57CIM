# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain import DateTime

class AssetGroupKind(Enum):
    ANALYSIS_GROUP = 1   #  "ANALYSISGROUP"
    INVENTORY_GROUP = 2   #  "INVENTORYGROUP"
    COMPLIANCE_GROUP = 3   #  "COMPLIANCEGROUP"
    FUNCTIONAL_GROUP = 4   #  "FUNCTIONALGROUP"
    OTHER = 5   #  "OTHER"

