package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MarketPlan.MarketFactors;
import IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode;

/**
 * Loss sensitivity applied to a ConnectivityNode for a given time interval.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class LossSensitivity extends MarketFactors {

	/**
	 * Loss penalty factor.
	 * Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental
	 * Transmission Loss expressed as a plus or minus value. The typical range of
	 * penalty factors is (0,9 to 1,1).
	 */
	public Float lossFactor;
	public MktConnectivityNode MktConnectivityNode;

	public LossSensitivity(){

	}
}//end LossSensitivity