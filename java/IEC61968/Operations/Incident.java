package IEC61968.Operations;

import IEC61970.Base.Domain.String;
import IEC61968.Customers.CustomerNotification;
import IEC61968.Customers.IncidentHazard;
import IEC61968.Work.Work;
import IEC61968.Common.Document;
import IEC61968.Common.Location;
import IEC61968.Common.Operator;

/**
 * Description of a problem in the field that may be reported in a trouble ticket
 * or come from another source. It may have to do with an outage.
 * @author Margaret
 * @created 03-Jan-2024 1:15:43 PM
 */
public class Incident extends Document {

	/**
	 * Cause of this incident.
	 */
	public String cause;
	/**
	 * All notifications for a customer related to the status change of this incident.
	 */
	public CustomerNotification CustomerNotifications;
	/**
	 * Outage for this incident.
	 */
	public Outage Outage;
	/**
	 * All hazards associated with this incident.
	 */
	public IncidentHazard IncidentHazard;
	/**
	 * All works addressing this incident.
	 */
	public Work Works;
	/**
	 * Location of this incident.
	 */
	public Location Location;
	/**
	 * Operator who owns this incident.
	 */
	public Operator Owner;

	public Incident(){

	}
}//end Incident