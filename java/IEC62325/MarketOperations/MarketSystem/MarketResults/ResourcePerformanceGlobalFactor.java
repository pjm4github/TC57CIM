package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Global factors are property/value pairs that are used to adjust resource
 * performance values. Example include scale factors (e.g. scale a baseline up or
 * down), adders (positive or negative), etc.
 * @author mwald
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class ResourcePerformanceGlobalFactor extends IdentifiedObject {

	/**
	 * Description (name) of the property (factor).
	 */
	public String factorDescription;
	/**
	 * Value of the property (factor).
	 */
	public String factorValue;
	public ResourcePerformanceEvaluation ResourcePerformanceEvaluation;

	public ResourcePerformanceGlobalFactor(){

	}
}//end ResourcePerformanceGlobalFactor