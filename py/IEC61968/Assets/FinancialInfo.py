from IEC61968.Assets.Asset import Asset
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.IntegerQuantity import IntegerQuantity
from IEC61970.Base.Domain.Money import Money


class FinancialInfo(IdentifiedObject):
    """
    #  * Various current financial properties associated with a particular asset.
    #  * Historical properties may be determined by ActivityRecords associated with the
    #  * asset.
    """
    def __init__(self):
        super().__init__()
        self.account = ""  # The account to which this actual material item is charged
        self.actual_purchase_cost = Money()  # The actual purchase cost of this particular asset
        self.cost_description = ""  # Description of the cost
        self.cost_type = ""  # Type of cost to which this Material Item belongs
        self.financial_value = Money()  # Value of asset as of 'valueDateTime'
        self.plant_transfer_date_time = DateTime()  # Date and time asset's financial value was put in plant
        self.purchase_date_time = DateTime()  # Date and time asset was purchased
        self.purchase_order_number = ""  # Purchase order identifier
        self.quantity = IntegerQuantity()  # The quantity of the asset if per unit length
        self.value_date_time = DateTime()  # Date and time at which the financial value was last established
        self.warranty_end_date_time = DateTime()  # Date and time warranty on asset expires
        self.asset = Asset()
