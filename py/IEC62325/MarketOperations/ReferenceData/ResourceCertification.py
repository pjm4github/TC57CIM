# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC62325.MarketOperations.MktDomain.MarketType import MarketType
from IEC62325.MarketOperations.MktDomain.ResourceCertificationKind import ResourceCertificationKind
from IEC62325.MarketOperations.MktDomain.YesNo import YesNo


class ResourceCertification:
    def __init__(self) -> None:
        self.market: MarketType = MarketType.DAM # market type
        self.qualification_flag: YesNo = YesNo.NO  # Status of the qualification ('Y' = Active, 'N' = Inactive)
        self.type: ResourceCertificationKind = ResourceCertificationKind.INTERMITTENT_RESOURCE # Type of service based on ResourceAncillaryServiceType enumeration

