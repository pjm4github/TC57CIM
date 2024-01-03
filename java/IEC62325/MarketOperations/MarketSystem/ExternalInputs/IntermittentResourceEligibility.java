package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.MarketPlan.MarketFactors;

/**
 * Indicates whether unit is eligible for treatment as a intermittent variable
 * renewable resource.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class IntermittentResourceEligibility extends MarketFactors {

	/**
	 * Indicates whether a resource is eligible for PIRP program for a given hour
	 */
	public String eligibilityStatus;

	public IntermittentResourceEligibility(){

	}
}//end IntermittentResourceEligibility