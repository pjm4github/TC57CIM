package IEC61968.Operations;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Integer;

/**
 * This defines the area covered by the Outage.
 * @author Margaret
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class OutageArea {

	/**
	 * This is the reported time of the first outage report
	 */
	public DateTime earliestReportedTime;
	/**
	 * defines the number of meters served in the defined area.
	 */
	public Integer metersServed;
	/**
	 * defines the type of area that has the outage - county, state, zipcode, etc.
	 */
	public AreaKind outageAreaKind;
	public Outage Outage;

	public OutageArea(){

	}
}//end OutageArea