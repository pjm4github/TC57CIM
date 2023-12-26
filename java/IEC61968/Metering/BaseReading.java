package IEC61968.Metering;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Meas.MeasurementValue;

/**
 * Common representation for reading values. Note that a reading value may have
 * multiple qualities, as produced by various systems ('ReadingQuality.source').
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public class BaseReading extends MeasurementValue {

	/**
	 * (used only when there are detailed auditing requirements) Date and time at
	 * which the reading was first delivered to the metering system.
	 */
	public DateTime reportedDateTime;
	/**
	 * System that originally supplied the reading (e.g., customer, AMI system,
	 * handheld reading system, another enterprise system, etc.).
	 */
	public String source;
	/**
	 * Start and end of the period for those readings whose type has a time attribute
	 * such as 'billing', seasonal' or 'forTheSpecifiedPeriod'.
	 */
	public DateTimeInterval timePeriod;
	/**
	 * Value of this reading.
	 */
	public String value;

	public BaseReading(){

	}
}//end BaseReading