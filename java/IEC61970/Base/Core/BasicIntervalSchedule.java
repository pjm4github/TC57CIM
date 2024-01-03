package IEC61970.Base.Core;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Domain.UnitSymbol;

/**
 * Schedule of values at points in time.
 * @created 02-Jan-2024 10:16:49 PM
 */
public class BasicIntervalSchedule extends IdentifiedObject {

	/**
	 * The time for the first time point.  The value can be a time of day, not a
	 * specific date.
	 */
	public DateTime startTime;
	/**
	 * Multiplier for value1.
	 */
	public UnitMultiplier value1Multiplier;
	/**
	 * Value1 units of measure.
	 */
	public UnitSymbol value1Unit;
	/**
	 * Multiplier for value2.
	 */
	public UnitMultiplier value2Multiplier;
	/**
	 * Value2 units of measure.
	 */
	public UnitSymbol value2Unit;

	public BasicIntervalSchedule(){

	}
}//end BasicIntervalSchedule