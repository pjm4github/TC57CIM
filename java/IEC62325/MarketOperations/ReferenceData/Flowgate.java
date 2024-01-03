package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MktDomain.InterTieDirection;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Core.PowerSystemResource;
import IEC62325.InfIEC62325.InfMarketResults.InterTieResults;
import IEC62325.InfIEC62325.InfCongestionRevenueRights.FTR;
import IEC62325.MarketOperations.MarketSystem.MarketResults.ConstraintResults;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.SecurityConstraints;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransmissionInterfaceRightEntitlement;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransmissionCapacity;
import IEC62325.MarketOperations.MarketOpCommon.MktLine;
import IEC62325.MarketOperations.MarketOpCommon.MktPowerTransformer;

/**
 * A flowgate, is single or group of transmission elements intended to model MW
 * flow impact relating to transmission limitations and transmission service usage.
 * 
 * @created 28-Dec-2023 12:12:12 PM
 */
public class Flowgate extends PowerSystemResource {

	/**
	 * The direction of the flowgate, export or import
	 */
	public InterTieDirection direction;
	/**
	 * Export MW rating
	 */
	public ActivePower exportMWRating;
	/**
	 * Import MW rating
	 */
	public ActivePower importMWRating;
	public FlowgateRelief FlowgateRelief;
	public InterTieResults InterTieResults;
	public FTR FTRs;
	public SchedulingPoint InterTie;
	public ContractDistributionFactor ContractDistributionFactor;
	public RegisteredInterTie RegisteredInterTie;
	public SubControlArea To_SubControlArea;
	public SubControlArea From_SubControlArea;
	public FlowgateValue FlowgateValue;
	public ConstraintResults ConstraintResults;
	public SecurityConstraints SecurityConstraints;
	public TransmissionInterfaceRightEntitlement TranmissionRightEntitlement;
	public TransmissionCapacity TransmissionCapacity;
	public MktLine MktLine;
	public MktPowerTransformer MktPowerTransformer;

	public Flowgate(){

	}
}//end Flowgate