package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode;

/**
 * This class models the system distribution factors. This class needs to be used
 * along with the HostControlArea and the ConnectivityNode to show the
 * distribution of each individual party.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class SysLoadDistributionFactor {

	/**
	 * Used to calculate load "participation" of a connectivity node in an host
	 * control area
	 */
	public Float factor;
	public MktConnectivityNode MktConnectivityNode;

	public SysLoadDistributionFactor(){

	}
}//end SysLoadDistributionFactor