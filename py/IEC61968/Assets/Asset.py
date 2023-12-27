# asset.py
from IEC61968.Assets.AcceptanceTest import AcceptanceTest
from IEC61968.Assets.AssetContainer import AssetContainer
from IEC61968.Assets.AssetDeployment import AssetDeployment
from IEC61968.Assets.AssetInfo import AssetInfo
from IEC61968.Assets.AssetKind import AssetKind
from IEC61968.Assets.AssetLifecycleStateKind import AssetLifecycleStateKind
from IEC61968.Assets.AssetOrganisationRole import AssetOrganisationRole
from IEC61968.Assets.InUseDate import InUseDate
from IEC61968.Assets.InUseStateKind import InUseStateKind
from IEC61968.Assets.LifecycleDate import LifecycleDate
from IEC61968.Assets.ProductAssetModel import ProductAssetModel
from IEC61968.Assets.RetiredReasonKind import RetiredReasonKind
from IEC61968.Common.ActivityRecord import ActivityRecord
from IEC61968.Common.ConfigurationEvent import ConfigurationEvent
from IEC61968.Common.Status import Status
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61970.Base.Domain.Money import Money
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Meas.Measurement import Measurement


class Asset(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.acceptance_test = AcceptanceTest()
        self.baseline_condition = ""
        self.baseline_loss_of_life = PerCent()
        self.critical = True
        self.electronic_address = ElectronicAddress()
        self.in_use_date = InUseDate()
        self.in_use_state = InUseStateKind.IN_USE
        self.kind = AssetKind.OTHER
        self.lifecycle_date = LifecycleDate()
        self.lifecycle_state = AssetLifecycleStateKind.RECEIVED
        self.lot_number = ""
        self.position = ""
        self.purchase_price = Money()
        self.retired_reason = RetiredReasonKind.OBSOLESCENCE
        self.serial_number = ""
        self.status = Status()
        self.type = ""
        self.utc_number = ""
        self.erp_inventory = ErpInventory()
        self.organisation_roles = AssetOrganisationRole()
        self.asset_function = AssetFunction()
        self.power_system_resources = PowerSystemResource()
        self.asset_container = AssetContainer()
        self.asset_property_curves = AssetPropertyCurve()
        self.erp_rec_delivery_items = ErpRecDelvLineItem()
        self.asset_deployment = AssetDeployment()
        self.reconditionings = Reconditioning()
        self.asset_info = AssetInfo()
        self.measurements = Measurement()
        self.product_asset_model = ProductAssetModel()
        self.configuration_events = ConfigurationEvent()
        self.location = Location()
        self.activity_records = ActivityRecord()
