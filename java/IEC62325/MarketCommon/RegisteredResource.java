package IEC62325.MarketCommon;

import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Hours;
import IEC62325.MarketOperations.MktDomain.ResourceRegistrationStatus;
import IEC62325.MarketOperations.ReferenceData.ForbiddenRegion;
import IEC62325.MarketOperations.ReferenceData.AggregateNode;
import IEC62325.MarketOperations.ParticipantInterfaces.DispatchInstReply;
import IEC62325.MarketManagement.TimeSeries;
import IEC62325.MarketOperations.ParticipantInterfaces.RampRateCurve;
import IEC62325.MarketOperations.ReferenceData.ContractDistributionFactor;
import IEC62325.MarketOperations.ReferenceData.OrgResOwnership;
import IEC62325.MarketOperations.MarketSystem.MarketResults.RMROperatorInput;
import IEC62325.MarketOperations.MarketSystem.MarketResults.ResourceDispatchResults;
import IEC62325.MarketOperations.ReferenceData.SubstitutionResourceList;
import IEC62325.MarketOperations.ReferenceData.AdjacentCASet;
import IEC62325.MarketOperations.ReferenceData.SubControlArea;
import IEC61970.Base.Core.PowerSystemResource;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.IntermittentResourceEligibility;
import IEC62325.MarketOperations.ReferenceData.FormerReference;
import IEC62325.MarketOperations.MarketSystem.MarketResults.Commitments;
import IEC62325.MarketOperations.MarketSystem.MarketResults.MPMResourceStatus;
import IEC62325.MarketOperations.MarketSystem.MarketResults.RUCAwardInstruction;
import IEC62325.MarketOperations.MarketQualitySystem.AllocationResultValues;
import IEC62325.MarketOperations.ParticipantInterfaces.LoadFollowingInst;
import IEC62325.MarketOperations.MarketSystem.MarketResults.ResourceLoadFollowingInst;
import IEC62325.MarketOperations.ReferenceData.ResourceCertification;
import IEC62325.MarketOperations.MarketQualitySystem.ExpectedEnergyValues;
import IEC62325.MarketManagement.Reason;
import IEC62325.InfIEC62325.InfMarketOperations.ResourceCertification;
import IEC62325.MarketOperations.ReferenceData.SchedulingPoint;
import IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode;
import IEC62325.InfIEC62325.InfExternalInputs.ResourceGroup;
import IEC62325.MarketOperations.MarketSystem.MarketResults.DopInstruction;

/**
 * A resource that is registered through the market participant registration
 * system. Examples include generating unit, load, and non-physical generator or
 * load.
 * @created 03-Jan-2024 1:57:22 PM
 */
public class RegisteredResource extends PowerSystemResource {

	/**
	 * Indication that this resource is associated with an Adjacent Control Area.
	 */
	public YesNo ACAFlag;
	/**
	 * Indication that the resource participates in the optimization process by
	 * default.
	 */
	public YesNo ASSPOptimizationFlag;
	/**
	 * Resource Commercial Operation Date. 
	 */
	public DateTime commercialOpDate;
	/**
	 * Contingent operating reserve availiability (Yes/No).  Resource is availiable to
	 * participate with capacity in contingency dispatch.
	 */
	public YesNo contingencyAvailFlag;
	/**
	 * Dispatchable: indicates whether the resource is dispatchable. This implies that
	 * the resource intends to submit Energy bids/offers or Ancillary Services
	 * bids/offers, or self-provided schedules.
	 */
	public Boolean dispatchable;
	/**
	 * Indication that this resource is associated with an Embedded Control area.
	 */
	public YesNo ECAFlag;
	/**
	 * Flexible offer flag (Y/N).
	 */
	public YesNo flexibleOfferFlag;
	/**
	 * Indicates need to dispatch before the start of the operating hour. Only
	 * relevant in Real-Time Market. Applies to generation, intertie and participating
	 * load resource. Value (Y/N).
	 */
	public YesNo hourlyPredispatch;
	/**
	 * A flag to indicate if a resource is an aggregated resource.
	 */
	public YesNo isAggregatedRes;
	/**
	 * Indication of the last time this item was modified/versioned.
	 */
	public DateTime lastModified;
	/**
	 * LMPM flag: indicates whether the resource is subject to the LMPM test (Yes/No).
	 */
	public YesNo LMPMFlag;
	/**
	 * Market Participation flag: indicates whether the resource participate in the
	 * market.
	 */
	public YesNo marketParticipationFlag;
	/**
	 * Maximum base self schedule quantity.
	 */
	public Float maxBaseSelfSchedQty ;
	/**
	 * Maximum on time after start up.
	 */
	public Float maxOnTime;
	/**
	 * Minimum number of consecutive hours a resource shall be dispatched if bid is
	 * accepted.  
	 */
	public Hours minDispatchTime;
	/**
	 * Minimum off time after shut down.
	 */
	public Float minOffTime;
	/**
	 * Minimum on time after start up.
	 */
	public Float minOnTime;
	/**
	 * Must offer flag: indicates whether the unit is subject to the must offer
	 * provisions (Y/N).
	 */
	public YesNo mustOfferFlag;
	/**
	 * Flag to indicate that the Resource is not participating in the Market
	 * Operations.
	 */
	public YesNo nonMarket;
	/**
	 * Indication that the registered resource is a Point of Delivery (YES) resource
	 * which implies there is a POD Loss Factor.
	 */
	public YesNo pointOfDeliveryFlag;
	/**
	 * Price setting flag: indicates whether a resource is capable of setting the
	 * Market Clearing Price (Y) for the DA market, and if not, indicates whether the
	 * resource shall submit bids for energy at $ 0 (S) or not (N).
	 * 
	 * Initially in the RegisteredGenerator class. It was moved to the
	 * RegisteredResource class for the participating load dispatch purpose.
	 */
	public YesNo priceSetFlagDA;
	/**
	 * Price setting flag: indicates whether a resource is capable of setting the
	 * Market Clearing Price (Y) for the RT market, and if not, indicates whether the
	 * resource shall submit bids for energy at $ 0 (S) or not (N).
	 * 
	 * Initially in the RegisteredGenerator class. It was moved to the
	 * RegisteredResource class for the participating load dispatch purpose.
	 */
	public YesNo priceSetFlagRT;
	/**
	 * Registration Status of resource - Active, Mothballed, Planned, or
	 * Decommissioned.
	 */
	public ResourceRegistrationStatus registrationStatus;
	/**
	 * Indication that this resource participates in the resource adequacy function.
	 */
	public YesNo resourceAdequacyFlag;
	/**
	 * SMPM flag: indicates whether the resource is subject to the SMPM test (Yes/No).
	 */
	public YesNo SMPMFlag;
	public ForbiddenRegion ForbiddenRegion;
	/**
	 * An AggregateNode may be associated with up to many RegisteredResources.
	 */
	public AggregateNode AggregateNode;
	public DispatchInstReply DispatchInstReply;
	public TimeSeries TimeSeries;
	public RampRateCurve RampRateCurve;
	public ContractDistributionFactor ContractDistributionFactor;
	public OrgResOwnership OrgResOwnership;
	public RMROperatorInput RMROperatorInput;
	public ResourceDispatchResults ResourceDispatchResults;
	public SubstitutionResourceList SubstitutionResourceList;
	public AdjacentCASet AdjacentCASet;
	public SubControlArea SubControlArea;
	public IntermittentResourceEligibility IntermittentResourceEligibility;
	public FormerReference FormerReference;
	public Commitments Commitments;
	public MPMResourceStatus MPMResourceStatus;
	public RUCAwardInstruction RUCAwardInstruction;
	public AllocationResultValues AllocationResultValues;
	public LoadFollowingInst LoadFollowingInst;
	public ResourceLoadFollowingInst ResourceLoadFollowingInst;
	/**
	 * RegisteredResources are qualified for resource ancillary service types (which
	 * include market product types as well as other types such as BlackStart) by the
	 * association to the class ResourceAncillaryServiceQualification.
	 */
	public ResourceCertification ResourceAncillaryServiceQualification;
	public ExpectedEnergyValues ExpectedEnergyValues;
	public Reason Reason;
	public ResourceCertification ResourceCertification;
	public SchedulingPoint InterTie;
	public MktConnectivityNode MktConnectivityNode;
	public ResourceGroup ResourceGroups;
	public DopInstruction DopInstruction;
	public MarketParticipant MarketParticipant;
	public ResourceCapacity ResourceCapacity;

	public RegisteredResource(){

	}
}//end RegisteredResource