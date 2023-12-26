package IEC61968.Metering;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Location;

/**
 * Location of an individual usage point.
 * @created 25-Dec-2023 8:45:25 PM
 */
public class UsagePointLocation extends Location {

	/**
	 * Method for the service person to access this usage point location. For example,
	 * a description of where to obtain a key if the facility is unmanned and secured.
	 */
	public String accessMethod;
	/**
	 * Remarks about this location.
	 */
	public String remark;
	/**
	 * Problems previously encountered when visiting or performing work at this
	 * location. Examples include: bad dog, violent customer, verbally abusive
	 * occupant, obstructions, safety hazards, etc.
	 */
	public String siteAccessProblem;
	/**
	 * All usage points at this location.
	 */
	public UsagePoint UsagePoints;

	public UsagePointLocation(){

	}
}//end UsagePointLocation