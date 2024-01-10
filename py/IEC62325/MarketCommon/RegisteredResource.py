from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Hours import Hours
from IEC62325.InfIEC62325.InfExternalInputs.ResourceGroup import ResourceGroup
from IEC62325.InfIEC62325.InfMarketOperations.ResourceCertification import ResourceCertification
from IEC62325.MarketCommon.MarketParticipant import MarketParticipant
from IEC62325.MarketCommon.ResourceCapacity import ResourceCapacity
from IEC62325.MarketManagement.Reason import Reason
from IEC62325.MarketManagement.TimeSeries import TimeSeries
from IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode import MktConnectivityNode
from IEC62325.MarketOperations.MarketQualitySystem.AllocationResultValues import AllocationResultValues
from IEC62325.MarketOperations.MarketQualitySystem.ExpectedEnergyValues import ExpectedEnergyValues
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.IntermittentResourceEligibility import \
    IntermittentResourceEligibility
from IEC62325.MarketOperations.MarketSystem.MarketResults.Commitments import Commitments
from IEC62325.MarketOperations.MarketSystem.MarketResults.DopInstruction import DopInstruction
from IEC62325.MarketOperations.MarketSystem.MarketResults.MPMResourceStatus import MPMResourceStatus
from IEC62325.MarketOperations.MarketSystem.MarketResults.RMROperatorInput import RMROperatorInput
from IEC62325.MarketOperations.MarketSystem.MarketResults.RUCAwardInstruction import RUCAwardInstruction
from IEC62325.MarketOperations.MarketSystem.MarketResults.ResourceDispatchResults import ResourceDispatchResults
from IEC62325.MarketOperations.MarketSystem.MarketResults.ResourceLoadFollowingInst import ResourceLoadFollowingInst
from IEC62325.MarketOperations.MktDomain.ResourceRegistrationStatus import ResourceRegistrationStatus
from IEC62325.MarketOperations.ParticipantInterfaces.DispatchInstReply import DispatchInstReply
from IEC62325.MarketOperations.ParticipantInterfaces.LoadFollowingInst import LoadFollowingInst
from IEC62325.MarketOperations.ParticipantInterfaces.RampRateCurve import RampRateCurve
from IEC62325.MarketOperations.ReferenceData.AdjacentCASet import AdjacentCASet
from IEC62325.MarketOperations.ReferenceData.AggregateNode import AggregateNode
from IEC62325.MarketOperations.ReferenceData.ContractDistributionFactor import ContractDistributionFactor
from IEC62325.MarketOperations.ReferenceData.ForbiddenRegion import ForbiddenRegion
from IEC62325.MarketOperations.ReferenceData.FormerReference import FormerReference
from IEC62325.MarketOperations.ReferenceData.OrgResOwnership import OrgResOwnership
from IEC62325.MarketOperations.ReferenceData.SchedulingPoint import SchedulingPoint
from IEC62325.MarketOperations.ReferenceData.SubControlArea import SubControlArea
from IEC62325.MarketOperations.ReferenceData.SubstitutionResourceList import SubstitutionResourceList


class RegisteredResource(PowerSystemResource):
    def __init__(self):
        super().__init__()
        self.aca_flag = False  # Indication that this resource is associated with an Adjacent Control Area.
        self.assp_optimization_flag = False  # Indication that the resource participates in the optimization process by default.
        self.commercial_op_date = DateTime()  # Resource Commercial Operation Date.
        self.contingency_avail_flag = False  # Contingent operating reserve availability (Yes/No). Resource is available to participate with capacity in contingency dispatch.
        self.dispatchable = False  # Dispatchable: indicates whether the resource is dispatchable. This implies that the resource intends to submit Energy bids/offers or Ancillary Services bids/offers, or self-provided schedules.
        self.eca_flag = False  # Indication that this resource is associated with an Embedded Control area.
        self.flexible_offer_flag = False  # Flexible offer flag (Y/N).
        self.hourly_predispatch = False  # Indicates need to dispatch before the start of the operating hour. Only relevant in Real-Time Market. Applies to generation, intertie and participating load resource. Value (Y/N).
        self.is_aggregated_res = False  # A flag to indicate if a resource is an aggregated resource.
        self.last_modified = DateTime()  # Indication of the last time this item was modified/versioned.
        self.lmpm_flag = False  # LMPM flag: indicates whether the resource is subject to the LMPM test (Yes/No).
        self.market_participation_flag = False  # Market Participation flag: indicates whether the resource participate in the market.
        self.max_base_self_sched_qty = 0.0  # Maximum base self schedule quantity.
        self.max_on_time = 0.0  # Maximum on time after start up.
        self.min_dispatch_time = Hours()  # Minimum number of consecutive hours a resource shall be dispatched if bid is accepted.
        self.min_off_time = 0.0  # Minimum off time after shut down.
        self.min_on_time = 0.0  # Minimum on time after start up.
        self.must_offer_flag = False  # Must offer flag: indicates whether the unit is subject to the must offer provisions (Y/N).
        self.non_market = False  # Flag to indicate that the Resource is not participating in the Market Operations.
        self.point_of_delivery_flag = False  # Indication that the registered resource is a Point of Delivery (YES) resource which implies there is a POD Loss Factor.
        self.price_set_flag_da = False  # Price setting flag: indicates whether a resource is capable of setting the Market Clearing Price (Y) for the DA market, and if not, indicates whether the resource shall submit bids for energy at $0 (S) or not (N).
        self.price_set_flag_rt = False  # Price setting flag: indicates whether a resource is capable of setting the Market Clearing Price (Y) for the RT market, and if not, indicates whether the resource shall submit bids for energy at $0 (S) or not (N).
        self.registration_status = ResourceRegistrationStatus.ACTIVE  # Registration Status of resource - Active, Mothballed, Planned, or Decommissioned.
        self.resource_adequacy_flag = False  # Indication that this resource participates in the resource adequacy function.
        self.smpm_flag = False  # SMPM flag: indicates whether the resource is subject to the SMPM test (Yes/No).
        self.forbidden_region = ForbiddenRegion()
        self.aggregate_node = AggregateNode()  # An AggregateNode may be associated with up to many RegisteredResources.
        self.dispatch_inst_reply = DispatchInstReply()
        self.time_series = TimeSeries()
        self.ramp_rate_curve = RampRateCurve()
        self.contract_distribution_factor = ContractDistributionFactor()
        self.org_res_ownership = OrgResOwnership()
        self.rmr_operator_input = RMROperatorInput()
        self.resource_dispatch_results = ResourceDispatchResults()
        self.substitution_resource_list = SubstitutionResourceList()
        self.adjacent_ca_set = AdjacentCASet()
        self.sub_control_area = SubControlArea()
        self.intermittent_resource_eligibility = IntermittentResourceEligibility()
        self.former_reference = FormerReference()
        self.commitments = Commitments()
        self.mpm_resource_status = MPMResourceStatus()
        self.ruca_award_instruction = RUCAwardInstruction()
        self.allocation_result_values = AllocationResultValues()
        self.load_following_inst = LoadFollowingInst()
        self.resource_load_following_inst = ResourceLoadFollowingInst()
        self.resource_ancillary_service_qualification = ResourceCertification()  # RegisteredResources are qualified for resource ancillary service types (which include market product types as well as other types such as BlackStart) by the association to the class ResourceAncillaryServiceQualification.
        self.expected_energy_values = ExpectedEnergyValues()
        self.reason = Reason()
        self.resource_certification = ResourceCertification()
        self.inter_tie = SchedulingPoint()
        self.mkt_connectivity_node = MktConnectivityNode()
        self.resource_groups = [ResourceGroup()]
        self.dop_instruction = DopInstruction()
        self.market_participant = MarketParticipant()
        self.resource_capacity = ResourceCapacity()
