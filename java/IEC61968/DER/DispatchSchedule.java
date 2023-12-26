package IEC61968.DER;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Core.CurveStyle;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.DateTime;

/**
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class DispatchSchedule {

	public PerCent confidence;
	/**
	 * Used to specify whether the values over an interval are constant
	 * (constantYValue) or linearly interpolated (straightLineYValues)
	 */
	public CurveStyle curveStyleKind;
	/**
	 * Used to specify the number of intervals when requesting a forecast or a
	 * dispatch.
	 */
	public Integer numberOfIntervals;
	/**
	 * The start time of the first interval in the dispatch schedule
	 */
	public DateTime startTime;
	/**
	 * The length of time for each interval in the dispatch schedule.
	 */
	public Integer timeIntervalDuration;
	/**
	 * The unit of measure for the time axis of the dispatch schedule.
	 */
	public TimeIntervalKind timeIntervalUnit;
	public DERMonitorableParameter DERMonitorableParameter;

	public DispatchSchedule(){

	}
}//end DispatchSchedule