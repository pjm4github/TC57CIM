package IEC62325.Environmental;

import IEC61968.Common.ActivityRecord;

/**
 * An environmental event to which one or more forecasts or observations may be
 * tied and which may relate to or affect one or more assets.
 * This class is intended to be used as a means of grouping forecasts and/or
 * observations and could be used for a variety of purposes, including:
 * <ul>
 * 	<li>to define a 'named' event like Hurricane Katrina and allow the historic
 * (or forecast) values for phenomena and measurements (precipitation,
 * temperature) across time to be  associated with it</li>
 * 	<li>to identify assets that were (or are forecast to be) affected by a
 * phenomenon or set of measurements</li>
 * </ul>
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class EnvironmentalEvent extends ActivityRecord {

	/**
	 * Forecast or observation related to this environmental event.
	 */
	public EnvironmentalInformation EnvironmentalInformation;

	public EnvironmentalEvent(){

	}
}//end EnvironmentalEvent