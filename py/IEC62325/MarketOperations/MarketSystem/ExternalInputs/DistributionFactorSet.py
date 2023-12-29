# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.GenDistributionFactor import GenDistributionFactor
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.LoadDistributionFactor import LoadDistributionFactor
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.SysLoadDistributionFactor import SysLoadDistributionFactor
from IEC62325.MarketOperations.MktDomain.MarketType import MarketType


class DistributionFactorSet:
    """
    A containing class that groups all the distribution factors within a market.
    *
    This is calculated daily for DA factors and hourly for RT factors.
    @created 27-Dec-2023 3:27:33 PM
    """

    def __init__(self) -> None:
        pass
        # * The end of the time interval for which requirement is defined.
        self.interval_end_time: DateTime = DateTime()
        # * The start of the time interval for which requirement is defined.
        self.interval_start_time: DateTime = DateTime()
        #  * Market type.
        self.market_type: MarketType = MarketType()
        self.gen_distribution_factor: GenDistributionFactor = GenDistributionFactor()
        self.sys_load_distribu_factor: SysLoadDistributionFactor = SysLoadDistributionFactor()
        self.load_distribution_factor: LoadDistributionFactor = LoadDistributionFactor()