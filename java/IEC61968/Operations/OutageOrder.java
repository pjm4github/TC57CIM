package IEC61968.Operations;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Document;
import IEC61968.Common.Location;

/**
 * Transmits an outage plan to a crew in order for the planned outage to be
 * executed.
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class OutageOrder extends Document {

	/**
	 * Free-form comment associated with the outage order
	 */
	public String comment;
	public Location Location;

	public OutageOrder(){

	}
}//end OutageOrder