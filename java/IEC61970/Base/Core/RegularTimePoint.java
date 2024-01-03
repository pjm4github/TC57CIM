package IEC61970.Base.Core;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Float;

/**
 * Time point for a schedule where the time between the consecutive points is
 * constant.
 * @created 02-Jan-2024 10:37:25 PM
 */
public class RegularTimePoint {

	/**
	 * The position of the regular time point in the sequence. Note that time points
	 * don't have to be sequential, i.e. time points may be omitted. The actual time
	 * for a RegularTimePoint is computed by multiplying the associated regular
	 * interval schedule's time step with the regular time point sequence number and
	 * adding the associated schedules start time.
	 */
	public Integer sequenceNumber;
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

	public RegularTimePoint(){

	}
}//end RegularTimePoint