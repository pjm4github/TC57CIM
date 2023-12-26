package IEC61968.Metering;

import IEC61968.Work.WorkTask;

/**
 * Work task involving meters.
 * @created 25-Dec-2023 8:45:23 PM
 */
public class MeterWorkTask extends WorkTask {

	/**
	 * Usage point to which this meter service work task applies.
	 */
	public UsagePoint UsagePoint;
	/**
	 * Meter on which this non-replacement work task is performed.
	 */
	public Meter Meter;
	/**
	 * Old meter replaced by this work task.
	 */
	public Meter OldMeter;

	public MeterWorkTask(){

	}
}//end MeterWorkTask