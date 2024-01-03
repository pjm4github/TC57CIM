package IEC61970.Base.Core;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Float;

/**
 * TimePoints for a schedule where the time between the points varies.
 * @created 02-Jan-2024 10:35:25 PM
 */
public class IrregularTimePoint {

	/**
	 * The time is relative to the schedule starting time.
	 */
	public Seconds time;
	/**
	 * The first value at the time. The meaning of the value is defined by the derived
	 * type of the associated schedule.
	 */
	public Float value1;
	/**
	 * The second value at the time. The meaning of the value is defined by the
	 * derived type of the associated schedule.
	 */
	public Float value2;

	public IrregularTimePoint(){

	}
}//end IrregularTimePoint