package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MarketSystem.ExternalInputs.GenDistributionFactor;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.LoadDistributionFactor;
import IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode;

/**
 * Individual pricing node based on Pnode.
 * @created 28-Dec-2023 12:15:18 PM
 */
public class IndividualPnode extends Pnode {

	public PnodeDistributionFactor PnodeDistributionFactor;
	public GenDistributionFactor GenDistributionFactor;
	public LoadDistributionFactor LoadDistributionFactor;
	public MktConnectivityNode MktConnectivityNode;

	public IndividualPnode(){

	}
}//end IndividualPnode