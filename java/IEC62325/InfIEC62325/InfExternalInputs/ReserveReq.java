package IEC62325.InfIEC62325.InfExternalInputs;

import IEC62325.MarketOperations.MarketPlan.MarketProduct;

/**
 * Requirements for minimum amount of reserve and/or regulation to be supplied by
 * a set of qualified resources.
 * @created 03-Jan-2024 1:51:06 PM
 */
public class ReserveReq extends ResourceGroupReq {

	public SensitivityPriceCurve SensitivityPriceCurve;
	/**
	 * Market product associated with reserve requirement must be a reserve or
	 * regulation product.
	 */
	public MarketProduct MarketProduct;

	public ReserveReq(){

	}
}//end ReserveReq