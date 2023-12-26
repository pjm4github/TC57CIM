package IEC61968.Operations;

import IEC61970.Base.Domain.Integer;

/**
 * Summary counts of service points affected by an outage. These counts are
 * sometimes referred to as total and critical customer count.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class ServicePointOutageSummary {

	/**
	 * Number of critical service (delivery) points affected by an outage.
	 */
	public Integer criticalCount;
	/**
	 * Number of all service (delivery) points affected by an outage.
	 */
	public Integer totalCount;

	public ServicePointOutageSummary(){

	}
}//end ServicePointOutageSummary