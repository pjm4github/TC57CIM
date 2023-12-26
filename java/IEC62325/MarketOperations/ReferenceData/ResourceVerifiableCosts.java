package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketCommon.RegisteredResource;

/**
 * This class is defined to describe the verifiable costs associated with a
 * generation resource.
 * @author USRAKHA
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class ResourceVerifiableCosts {

	public MktHeatRateCurve MktHeatRateCurve;
	public RegisteredResource RegisteredResource;
	public ResourceStartupCost ResourceStartupCost;

	public ResourceVerifiableCosts(){

	}
}//end ResourceVerifiableCosts