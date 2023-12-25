from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.ProductAssetModel import ProductAssetModel
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Equipment import Equipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class OperationalRestriction(Document):
    """
    A document that can be associated with equipment to describe any sort of
    restrictions compared with the original manufacturer's specification or with
    the usual operational practice e.g. temporary maximum loadings, maximum
    switching current, do not operate if bus couplers are open, etc.
    In the UK, for example, if a breaker or switch ever mal-operates, this is
    reported centrally and utilities use their asset systems to identify all the
    installed devices of the same manufacturer's type. They then apply operational
    restrictions in the operational systems to warn operators of potential problems.
    After appropriate inspection and maintenance, the operational restrictions may
    be removed.
    """

    def __init__(self):
        """
        Constructor for OperationalRestriction.
        """
        super().__init__()
        self.active_period = DateTimeInterval()
        """
        Interval during which this restriction is applied.
        """

        self.restricted_value = 0.0
        """
        Restricted (new) value; includes unit of measure and potentially multiplier.
        """

        self.equipments = Equipment()
        """
        All equipments to which this restriction applies.
        """

        self.product_asset_model = ProductAssetModel()
        """
        Asset model to which this restriction applies.
        """
