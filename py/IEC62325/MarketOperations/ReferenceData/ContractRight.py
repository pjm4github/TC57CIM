# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 13:18:10 2023
from IEC61970.Base.Domain.CostPerEnergyUnit import CostPerEnergyUnit
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.TREntitlement import TREntitlement
from IEC62325.MarketOperations.MktDomain.ContractType import ContractType
from IEC62325.MarketOperations.MktDomain.MarketType import MarketType
from IEC62325.MarketOperations.MktDomain.TRType import TRType
from IEC62325.MarketOperations.MktDomain.YesNo import YesNo
from IEC62325.MarketOperations.ParticipantInterfaces.BidSelfSched import BidSelfSched
from IEC62325.MarketOperations.ReferenceData.ContractDistributionFactor import ContractDistributionFactor
from IEC62325.MarketOperations.ReferenceData.SubstitutionResourceList import SubstitutionResourceList


class ContractRight:
    """
    Provides definition of Transmission Ownership Right and Existing Transmission
    Contract identifiers for use by SCUC. RMR contract hosting: Startup lead time,
    Contract Service Limits, Max Service Hours, Max MWhs, Max Start-ups, Ramp Rate,
    Max Net Dependable Capacity, Min Capacity and Unit Substitution for DAM/RTM to
    retrieve.
    @created 28-Dec-2023 1:03:47 PM
    """

    def __init__(self):
        self.chain_order = 0  # When used in conjunction with a Transmission Right contract chain, this is the
        # precedence for the contracts.
        self.contract_mw = 0.0  # MW value of the contract
        self.contract_price = CostPerEnergyUnit()  # Financial value of the contract
        self.contract_priority = 0  # Priority for the contract. This should be unique among all contracts for a
        # specific resource. This value is the directive for the SCUC algorithm on the order to satisfy/cut contracts.
        self.contract_status = ""  # Contract status
        self.contract_type = ContractType.TE  # type of the contract. Possible values are but not limited by: ETC,
        # TOR or RMR and RMT self schedules
        self.financial_location = YesNo.NO  # Indicator if the location associated with this contract is financial (
        # e.g. pricing nodes) or physical (e.g. connectivity nodes).
        self.financial_rights_dam = YesNo.NO  # Flag to indicate this contract provides financial rights in the DA
        # Market
        self.financial_rights_rtm = YesNo.NO  # Flag to indicate this contract provides financial rights in the RT
        # Market
        self.fuel_adder = 0.0  # Estimated Fuel Adder
        self.latest_sched_minutes = 0  # This indicates the latest schedule minutes (e.g. t - xx) that this resource
        # can be notified to respond. This attribute is only used if the market type is not supplied.
        self.latest_sched_mkt_type = MarketType.DAM  # This indicates the latest schedule market type a contract can
        # be applied to. This is used in conjunction with the latestSchedMinutes attribute to determine the latest
        # time this contract can be called in. The possible values for this attribute are: DAM, RTM, or it can be
        # omitted. If omitted, the latestSchedMinutes attribute defines the value.
        self.maximum_schedule_quantity = 0.0  # Maximum schedule MW quantity
        self.maximum_service_hours = 0  # Maximum service hours
        self.maximum_startups = 0  # Maximum startups
        self.max_net_dependable_capacity = 0.0  # Maximum Net Dependable Capacity
        self.minimum_load = 0.0  # Minimum Load
        self.minimum_schedule_quantity = 0.0  # Minimum schedule quantity
        self.physical_rights_dam = YesNo.NO  # Flag to indicate this contract provides physical rights in the DA Market
        self.physical_rights_rtm = YesNo.NO  # Flag to indicate this contract provides physical rights in the RT Market
        self.startup_lead_time = 0  # Start up lead time
        self.tr_type = TRType.CHAIN  # Transmission Right type - is this an individual contract right or a chain
        # contract right. Types = CHAIN or INDIVIDUAL
        self.substitution_resource_list = SubstitutionResourceList()
        self.contract_distribution_factor = ContractDistributionFactor()
        self.bid_self_sched = BidSelfSched()
        self.tr_entitlement = TREntitlement()
