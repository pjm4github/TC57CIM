package IEC61968.Customers;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Boolean;
import IEC61968.Metering.EndDevice;
import IEC61968.Metering.UsagePoint;
import IEC61968.Work.WorkLocation;

/**
 * A real estate location, commonly referred to as premises.
 * @created 03-Jan-2024 12:17:58 PM
 */
public class ServiceLocation extends WorkLocation {

	/**
	 * Method for the service person to access this service location. For example, a
	 * description of where to obtain a key if the facility is unmanned and secured.
	 */
	public String accessMethod;
	/**
	 * True if inspection is needed of facilities at this service location. This could
	 * be requested by a customer, due to suspected tampering, environmental concerns
	 * (e.g., a fire in the vicinity), or to correct incompatible data.
	 */
	public Boolean needsInspection;
	/**
	 * Problems previously encountered when visiting or performing work on this
	 * location. Examples include: bad dog, violent customer, verbally abusive
	 * occupant, obstructions, safety hazards, etc.
	 */
	public String siteAccessProblem;
	/**
	 * All end devices that measure the service delivered to this service location.
	 */
	public EndDevice EndDevices;
	/**
	 * All usage points delivering service (of the same type) to this service location.
	 */
	public UsagePoint UsagePoints;
	public TroubleTicket TroubleTicket;

	public ServiceLocation(){

	}
}//end ServiceLocation