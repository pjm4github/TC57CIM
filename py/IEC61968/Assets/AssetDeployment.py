# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.BreakerApplicationKind import BreakerApplicationKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.DeploymentDate import DeploymentDate
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.DeploymentStateKind import DeploymentStateKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.FacilityKind import FacilityKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.TransformerApplicationKind import TransformerApplicationKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.BaseVoltage import BaseVoltage


class AssetDeployment(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.breaker_application = BreakerApplicationKind.OTHER
        self.deployment_date = DeploymentDate()
        self.deployment_state = DeploymentStateKind.IN_SERVICE
        self.facility_kind = FacilityKind.DISTRIBUTION_POLE_TOP
        self.likelihood_of_failure = 0
        self.transformer_application = TransformerApplicationKind.GENERATOR_STEP_UP
        self.base_voltage = BaseVoltage()
