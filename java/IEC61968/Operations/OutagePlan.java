package IEC61968.Operations;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Domain.String;
import IEC61968.Common.Document;

/**
 * Document containing the definition of planned outages of equipment and/or usage
 * points. It will reference switching plans that are used to execute the planned
 * outage.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class OutagePlan extends Document {

	/**
	 * The date and time the outage plan was approved
	 */
	public DateTime approvedDateTime;
	/**
	 * Date and Time the planned outage was canceled.
	 */
	public DateTime cancelledDateTime;
	/**
	 * planned start and end time of the planned outage.
	 */
	public DateTimeInterval plannedPeriod;
	/**
	 * Purpose of  this outage plan, such as whether it is to replace equipment or
	 * perform maintenance or repairs or to reconfigure network topology.
	 */
	public String purpose;
	public OutageOrder OutageOrder;
	/**
	 * The outage resulting from the execution of the outage plan.
	 */
	public PlannedOutage PlannedOutage;

	public OutagePlan(){

	}
}//end OutagePlan