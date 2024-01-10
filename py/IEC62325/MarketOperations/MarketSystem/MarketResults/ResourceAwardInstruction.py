# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource
from IEC62325.MarketOperations.MarketSystem.MarketResults.SelfScheduleBreakdown import SelfScheduleBreakdown
from IEC62325.MarketOperations.MktDomain.MQSCHGType import MQSCHGType
from IEC62325.MarketOperations.MktDomain.YesNo import YesNo


class ResourceAwardInstruction:
    """
    Model of market results, instruction for resource.  Contains details of award
    as attributes.
    """
    
    def __init__(self) -> None:
        self.award_mw: float = 0.0
        """
        For DA Energy: Not Applicable;
        For DA AS: DA AS market award;
        For RT Energy: Not Applicable;
        For RT AS: RT AS market award (excluding DA AS market or self-proviison awards)
        """

        self.cleared_mw: float = 0.0
        """
        For DA Energy: Total Schedule = DA market schedule + DA self-schedule award;
        For DA AS: DA Ancillary Service Awards = DA AS market award + DA AS self-provision award;
        For RT Energy: Total Schedule = RT market schedule + RT self-schedule award;
        For RT AS: RT Ancillary Service Awards = RT AS self-provision award + RT AS market award + DA AS market award + DA AS self-provision award;
        """

        self.cleared_price: float = 0.0
        """
        Marginal Price ($/MW) for the commodity (Regulation Up, Regulation Down,
        Spinning Reserve, or Non-spinning reserve) for pricing run.
        """

        self.congest_lmp: float = 0.0
        """
        Congestion component of Location Marginal Price (LMP) in monetary units per MW.
        """

        self.cost_lmp: float = 0.0
        """
        Cost component of Locational Marginal Pricing (LMP) in monetary units per MW.
        """

        self.dispatcher_added_mw: float = 0.0
        """
        The tier2 mw added by dispatcher action
        Market results of the synchronized reserve market
        """

        self.economic_max: float = 0.0
        """
        Unit max output for dispatch; bid in economic maximum
        """

        self.economic_min: float = 0.0
        """
        Unit min output for dispatch; bid in economic minimum
        """

        self.eff_regulation_down_limit: float = 0.0
        """
        Effective Regulation Down Limit (MW)
        """

        self.eff_regulation_up_limit: float = 0.0
        """
        Effective Regulation Up Limit
        """

        self.lmp: float = 0.0
        """
        Locational marginal price value
        """

        self.loss_lmp: float = 0.0
        """
        Loss component of Location Marginal Price (LMP) in monetary units per MW.
        """

        self.manually_blocked: Optional[YesNo] = YesNo.NO
        """
        Indicates if an award was manually blocked (Y/N). Valid for Spinning and
        Non-spinning.
        """

        self.marginal_resource_indicator: Optional[YesNo] = YesNo.YES
        """
        Indicator (Yes / No) that this resource set the price for this dispatch /
        schedule.
        """

        self.must_run_ind: bool = True
        """
        Identifes if the unit was set to must run by the market participant responsible
        for bidding in the unit
        """

        self.no_load_cost: float = 0.0
        """
        Unit no-load cost in case of energy commodity
        """

        self.optimal_bid_cost: float = 0.0
        """
        Optimal Bid cost
        """

        self.optimal_bid_pay: float = 0.0
        """
        Optimal Bid production payment based on LMP
        """

        self.optimal_margin: float = 0.0
        """
        Optimal Bid production margin
        """

        self.override_time_stamp: DateTime = DateTime()
        """
        Time the manual data entry occured.
        """

        self.override_value: float = 0.0
        """
        Provides the ability for the grid operator to override items, such as spin
        capacity requirements, prior to running the algorithm. This value is market
        product based (spin, non-spin, reg up, reg down, or RUC).
        """

        self.self_sched_mw: float = 0.0
        """
        For DA Energy: DA total self-schedule award;
        For DA AS: DA AS self-provision award;
        For RT Energy: RT total self-schedule award;
        For RT AS: RT AS self-provision award (excluding DA AS market or self-provision
        awards)
        """

        self.start_up_cost: float = 0.0
        """
        Unit start up cost in case of energy commodity
        """

        self.status: str = ""
        """
        In or out status of resource
        """

        self.total_revenue: float = 0.0
        """
        Total bid revenue (startup_cost + no_load_cost + bid_pay)
        """

        self.update_time_stamp: DateTime = DateTime()
        self.update_type: Optional[MQSCHGType] = MQSCHGType.ADD
        self.update_user: str = ""

        self.self_schedule_breakdown: Optional[SelfScheduleBreakdown] = SelfScheduleBreakdown()
        self.registered_resource: Optional[RegisteredResource] = RegisteredResource()
