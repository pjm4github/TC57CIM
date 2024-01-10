# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023


from IEC61968.Common.Document import Document
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketCommon.MarketParticipant import MarketParticipant
from IEC62325.MarketOperations.MarketPlan.EnergyMarket import EnergyMarket
from IEC62325.MarketOperations.MarketSystem.MarketResults.ChargeProfile import ChargeProfile
from IEC62325.MarketOperations.MarketSystem.MarketResults.MitigatedBidSegment import MitigatedBidSegment
from IEC62325.MarketOperations.MktDomain.MarketType import MarketType


class Bid(Document):
    def __init__(self) -> None:
        super().__init__()
        self.market_type: MarketType = MarketType.DAM
        self.start_time: DateTime = DateTime()
        self.stop_time: DateTime = DateTime()
        self.charge_profiles: ChargeProfile = ChargeProfile()
        self.mitigated_bid_segment: MitigatedBidSegment = MitigatedBidSegment()
        self.energy_market: EnergyMarket = EnergyMarket()
        self.market_participant: MarketParticipant = MarketParticipant()
