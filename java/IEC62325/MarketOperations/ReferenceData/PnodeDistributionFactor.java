package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.YesNo;

/**
 * This class allows SC to input different distribution factors for pricing node.
 * @created 28-Dec-2023 12:19:30 PM
 */
public class PnodeDistributionFactor {

	/**
	 * Used to calculate "participation" of Pnode in an AggregatePnode. For example,
	 * for regulation region this factor is 1 and total sum of all factors for a
	 * specific regulation region does not have to be 1. For pricing zone the total
	 * sum of all factors has to be 1.
	 */
	public Float factor;
	/**
	 * Indication that this distribution factor is to apply during off peak.
	 */
	public YesNo offPeak;
	/**
	 * Indication that this factor is to apply during Peak periods.
	 */
	public YesNo onPeak;
	/**
	 * Point of delivery loss factor
	 */
	public Float podLossFactor;

	public PnodeDistributionFactor(){

	}
}//end PnodeDistributionFactor