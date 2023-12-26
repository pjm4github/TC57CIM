package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.PerCent;

/**
 * Representing the ratio of the load share for the associated SC.
 * @author USRAKHA
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class LoadRatio {

	/**
	 * Interval End Time
	 */
	public DateTime intervalEndTime;
	/**
	 * Interval Start Time
	 */
	public DateTime intervalStartTime;
	/**
	 * Share in percentage of total Market load for the selected time interval.
	 */
	public PerCent share;
	public SchedulingCoordinator SchedulingCoordinator;

	public LoadRatio(){

	}
}//end LoadRatio