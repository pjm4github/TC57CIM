package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.EquipmentStatusType;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * Model of ex-post pricing of resources contains components of LMPs: energy,
 * congestion, loss. Resource based.
 * @created 28-Dec-2023 8:21:11 PM
 */
public class ExPostResourceResults {

	/**
	 * LMP component in USD (deprecated)
	 */
	public Float congestionLMP;
	/**
	 * Desired output of unit
	 */
	public Float desiredMW;
	/**
	 * Unit Dispatch rate from real time unit dispatch.
	 */
	public Float dispatchRate;
	/**
	 * LMP (Local Marginal Price) in USD at the equipment (deprecated)
	 */
	public Float lmp;
	/**
	 * loss lmp (deprecated)
	 */
	public Float lossLMP;
	/**
	 * Economic Maximum MW
	 */
	public Float maxEconomicMW;
	/**
	 * Economic Minimum MW
	 */
	public Float minEconomicMW;
	/**
	 * Current MW output of the equipment
	 * Attribute Usage: Information purposes - Information purposes - Output of LPA
	 * engine.
	 */
	public Float resourceMW;
	/**
	 * Status of equipment 
	 */
	public EquipmentStatusType status;
	public ExPostResource ExPostResource;
	public RegisteredResource RegisteredResource;

	public ExPostResourceResults(){

	}
}//end ExPostResourceResults