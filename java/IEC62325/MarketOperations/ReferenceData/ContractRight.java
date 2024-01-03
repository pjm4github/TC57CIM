package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.CostPerEnergyUnit;
import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.MktDomain.ContractType;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC62325.MarketOperations.MktDomain.MarketType;
import IEC62325.MarketOperations.MktDomain.TRType;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.ParticipantInterfaces.BidSelfSched;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.TREntitlement;

/**
 * Provides definition of Transmission Ownership Right and Existing Transmission
 * Contract identifiers for use by SCUC. RMR contract hosting: Startup lead time,
 * Contract Service Limits, Max Service Hours, Max MWhs, Max Start-ups, Ramp Rate,
 * Max Net Dependable Capacity, Min Capacity and Unit Substitution for DAM/RTM to
 * retrieve.
 * @created 03-Jan-2024 2:15:33 PM
 */
public class ContractRight extends IdentifiedObject {

	/**
	 * When used in conjunction with a Transmission Right contract chain, this is the
	 * precedence for the contracts.
	 */
	public Integer chainOrder;
	/**
	 * MW value of the contract
	 */
	public Float contractMW;
	/**
	 * Financial value of the contract
	 */
	public CostPerEnergyUnit contractPrice;
	/**
	 * Priority for the contract. This should be unique amoung all contracts for a
	 * specific resource. This value is the directive for the SCUC algorithm on the
	 * order to satisfy/cut contracts.
	 */
	public Integer contractPriority;
	/**
	 * Contract status
	 */
	public String contractStatus;
	/**
	 * type of the contract. Possible values are but not limited by:
	 * 
	 * ETC, TOR or RMR and RMT self schedules
	 */
	public ContractType contractType;
	/**
	 * Indicator if the location associated with this contract is financial (e.g.
	 * pricing nodes) or physical (e.g. connectivity nodes).
	 */
	public YesNo financialLocation;
	/**
	 * Flag to indicate this contract provides financial rights in the DA Market
	 */
	public YesNo financialRightsDAM;
	/**
	 * Flag to indicate this contract provides financial rights in the RT Market
	 */
	public YesNo financialRightsRTM;
	/**
	 * Estimated Fuel Adder
	 */
	public Float fuelAdder;
	/**
	 * This indicates the latest schedule minutes (e.g. t - xx) that this resource can
	 * be notified to respond. This attribute is only used if the market type is not
	 * supplied. 
	 */
	public Integer latestSchedMinutes;
	/**
	 * This indicates the latest schedule market type a contract can be applied to.
	 * This is used in conjunction with the latestSchedMinutes attribute to determine
	 * the latest time this contract can be called in. The possible values for this
	 * attribute are: DAM, RTM or it can be omitted. If omitted, the
	 * latestSchedMinutes attribute defines the value.
	 */
	public MarketType latestSchedMktType;
	/**
	 * Maximum schedule MW quantity
	 */
	public Float maximumScheduleQuantity;
	/**
	 * Maximum service hours
	 */
	public Integer maximumServiceHours;
	/**
	 * Maximum startups
	 */
	public Integer maximumStartups;
	/**
	 * Maximum Net Dependable Capacity
	 */
	public Float maxNetDependableCapacity;
	/**
	 * Minimum Load
	 */
	public Float minimumLoad;
	/**
	 * Minimum schedule quanity
	 */
	public Float minimumScheduleQuantity;
	/**
	 * Flag to indicate this contract provides physical rights in the DA Market
	 */
	public YesNo physicalRightsDAM;
	/**
	 * Flag to indicate this contract provides physical rights in the RT Market
	 */
	public YesNo physicalRightsRTM;
	/**
	 * Start up lead time
	 */
	public Integer startupLeadTime;
	/**
	 * Transmission Right type - is this an individual contract right or a chain
	 * contract right. Types = CHAIN or INDIVIDUAL
	 */
	public TRType TRType;
	public SubstitutionResourceList SubstitutionResourceList;
	public ContractDistributionFactor ContractDistributionFactor;
	public BidSelfSched BidSelfSched;
	public TREntitlement TREntitlement;

	public ContractRight(){

	}
}//end ContractRight