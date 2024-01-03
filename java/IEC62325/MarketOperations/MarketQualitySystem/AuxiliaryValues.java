package IEC62325.MarketOperations.MarketQualitySystem;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.YesNo;

/**
 * Models Auxiliary Values.
 * @created 03-Jan-2024 2:07:09 PM
 */
public class AuxiliaryValues extends AuxiliaryObject {

	public Float availUndispatchedQ;
	public Float incrementalORAvail;
	public Float maxExpostCapacity;
	public Float minExpostCapacity;
	public Float noLoadCost;
	public YesNo noLoadCostEligibilityFlag;
	public Float startUpCost;
	public YesNo startUpCostEligibilityFlag;

	public AuxiliaryValues(){

	}
}//end AuxiliaryValues