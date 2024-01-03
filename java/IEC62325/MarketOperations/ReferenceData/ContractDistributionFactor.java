package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.YesNo;

/**
 * Distribution among resources at the sink point or source point.
 * @created 03-Jan-2024 2:15:33 PM
 */
public class ContractDistributionFactor {

	/**
	 * MW value that this resource provides to the overall contract.
	 */
	public Float factor;
	/**
	 * This value will be set to YES if the referenced Cnode is defined as the sink
	 * point in the contract.
	 */
	public YesNo sinkFlag;
	/**
	 * This value will be set to YES if the referenced Cnode is defined as the source
	 * point in the contract.
	 */
	public YesNo sourceFlag;

	public ContractDistributionFactor(){

	}
}//end ContractDistributionFactor