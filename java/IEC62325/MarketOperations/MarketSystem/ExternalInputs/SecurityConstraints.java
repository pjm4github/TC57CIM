package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.ActivePower;
import IEC62325.MarketOperations.ReferenceData.RTO;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Typical for regional transmission operators (RTOs), these constraints include
 * transmission as well as generation group constraints identified in both base
 * case and critical contingency cases.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class SecurityConstraints extends IdentifiedObject {

	/**
	 * Actual branch or group of branches MW flow (only for transmission constraints)
	 */
	public ActivePower actualMW;
	/**
	 * Maximum MW limit
	 */
	public ActivePower maxMW;
	/**
	 * Minimum MW limit (only for transmission constraints).
	 */
	public ActivePower minMW;
	public RTO RTO;

	public SecurityConstraints(){

	}
}//end SecurityConstraints