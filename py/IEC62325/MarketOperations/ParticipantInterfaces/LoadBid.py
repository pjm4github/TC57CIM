# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.ActivePowerChangeRate import ActivePowerChangeRate
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Money import Money
from IEC62325.MarketOperations.ParticipantInterfaces.LoadReductionPriceCurve import LoadReductionPriceCurve
from IEC62325.MarketOperations.ParticipantInterfaces.RampRateCurve import RampRateCurve
from IEC62325.MarketOperations.ParticipantInterfaces.ResourceBid import ResourceBid


class LoadBid(ResourceBid):
    def __init__(self) -> None:
        super().__init__()
        self.drop_ramp_rateOptional[ActivePowerChangeRate] = ActivePowerChangeRate()  # Maximum rate that load can be reduced (MW/minute)
        self.load_red_initiation_costOptional[Money] = Money()  # Load reduction initiation cost
        self.load_red_initiation_timeOptional[float] = 0.0  # Load reduction initiation time
        self.market_dateOptional[DateTime] = DateTime()   # The date represents the NextMarketDate for which the load response bids apply to
        self.metered_valueOptional[bool] = False  # Flag indicated that the load reduction is metered (See above). If priceSetting and meteredValue both equal 1, then the facility is eligible to set LMP in the real time market.
        self.min_loadOptional[ActivePower] = ActivePower()  # Minimum MW load below which it may not be reduced
        self.min_load_reductionOptional[ActivePower] = ActivePower()  # Minimum MW for a load reduction (e.g. MW rating of a discrete pump)
        self.min_load_reduction_costOptional[Money] = Money()  # Cost in $ at the minimum reduced load
        self.min_load_reduction_intervalOptional[float] = 0.0  # Shortest period load reduction shall be maintained before load can be restored to normal levels
        self.min_time_bet_load_redOptional[float] = 0.0  # Shortest time that load shall be left at normal levels before a new load reduction
        self.pick_up_ramp_rateOptional[ActivePowerChangeRate] = ActivePowerChangeRate()  # Maximum rate load may be restored (MW/minute)
        self.price_settingOptional[bool] = False  # Flag to indicate that the facility can set LMP. Works in tandem with Metered Value
        self.req_notice_timeOptional[float] = 0.0  # Time period that is required from an order to reduce a load to the time that it takes to get to the minimum load reduction
        self.shutdown_costOptional[Money] = Money()  # The fixed cost associated with committing a load reduction
        self.load_reduction_price_curveOptional[LoadReductionPriceCurve] = LoadReductionPriceCurve()
        self.ramp_rate_curveOptional[RampRateCurve] = RampRateCurve()
