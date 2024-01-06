from IEC61968.Common.OrganisationRole import OrganisationRole
from IEC61968.Common.Status import Status
from IEC62325.MarketOperations.CongestionRevenueRights.CongestionRevenueRight import CongestionRevenueRight
from IEC62325.MarketOperations.MktDomain.CRRRoleType import CRRRoleType


class CRROrgRole(OrganisationRole):
    """
    Identifies a way in which an organisation may participate with a defined
    Congestion Revenue Right (CRR).
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.kind = CRRRoleType.SELLER  # Kind of role the organisation is with regards to the congestion revenue rights.
        self.status = Status()  # Status of congestion revenue rights organisation role.
        self.congestion_revenue_right = CongestionRevenueRight()  # Associated CongestionRevenueRight
