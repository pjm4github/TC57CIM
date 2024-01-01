# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PerCent import PerCent
from IEC62325.MarketOperations.ReferenceData.ResourceCertification import YesNo


class OrgResOwnership(IdentifiedObject):
    """
    This class models the ownership percent and type of ownership between resource and organisation.
    @created 28-Dec-2023 12:19:05 PM
    """

    def __init__(self) -> None:
        """
        Constructor for OrgResOwnership
        """
        super().__init__()
        self.assc_typeOptional[ResourceAssnType] = ResourceAssnType  # association type for the association between Organisation and Resource
        self.master_scheduling_coordinator_flagOptional[YesNo] = YesNo.NO  # Flag to indicate that the SC representing the Resource is the Master SC
        self.ownership_percentOptional[PerCent] = PerCent()  # ownership percentage for each resource
