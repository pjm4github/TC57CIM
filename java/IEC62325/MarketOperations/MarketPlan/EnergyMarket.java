package IEC62325.MarketOperations.MarketPlan;

import IEC62325.MarketOperations.ReferenceData.RTO;
import IEC62325.MarketOperations.MarketSystem.MarketResults.Settlement;
import IEC62325.MarketOperations.MarketSystem.MarketResults.MarketResults;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * Energy and Ancillary Market (e.g. Energy, Spinning Reserve, Non-Spinning
 * Reserve) with a description of the Market operation control parameters.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class EnergyMarket extends Market {

	public RTO RTO;
	public Settlement Settlements;
	public MarketResults MarketResults;
	public RegisteredResource RegisteredResources;

	public EnergyMarket(){

	}
}//end EnergyMarket