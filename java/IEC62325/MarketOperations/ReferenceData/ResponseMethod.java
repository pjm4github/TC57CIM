package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Specifies a category of energy usage that the demand response applies for; e.g.
 * energy from lighting, HVAC, other.
 * @author mwald
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class ResponseMethod extends IdentifiedObject {

	/**
	 * The active power value for the demand adjustment type. This supports requests
	 * to be made to a resource for some amount of active power provided by a
	 * particular response method, as specified by the method attribute (e.g. lighting,
	 * HVAC, wall mounted air conditioners, etc.).
	 */
	public Float activePower;
	/**
	 * The unit of measure of active power, e.g. kiloWatts (kW), megaWatts (mW), etc.
	 */
	public String activePowerUOM;
	/**
	 * The response method (e.g. lighting, HVAC, wall mounted air conditioners, etc.).
	 */
	public String method;
	/**
	 * This value provides for scaling of a response method's active power. For
	 * example, a response method of air conditioning could utilize a small amount of
	 * active power from each air conditioning unit (e.g. 0.1 kiloWatt), but the site
	 * multiplier could be used to produce a the total active power adjustment by
	 * multiplying the response method active power by this value (e.g. a building
	 * with 100 window air conditioning  units, so 100 * 0.1 kW = 10 kW).
	 */
	public Integer siteMultiplier;
	public RegisteredDistributedResource RegisteredResource;

	public ResponseMethod(){

	}
}//end ResponseMethod