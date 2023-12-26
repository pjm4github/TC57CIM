package IEC61968.Operations;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTimeInterval;
import IEC61968.Common.Document;
import IEC61968.Common.Location;

/**
 * Trouble order sends an incident to a crew to initiate a response to an
 * unplanned outage.
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class TroubleOrder extends Document {

	/**
	 * Free-form comment associated with the trouble order.
	 */
	public String comment;
	/**
	 * The planned start and end time for the trouble order. 
	 */
	public DateTimeInterval plannedExecutionInterval;
	public Incident Incident;
	public Location Location;

	public TroubleOrder(){

	}
}//end TroubleOrder