package IEC61970.Base.Core;


/**
 * The schedule has time points where the time between them varies.
 * @created 02-Jan-2024 10:35:14 PM
 */
public class IrregularIntervalSchedule extends BasicIntervalSchedule {

	/**
	 * The point data values that define a curve.
	 */
	public IrregularTimePoint TimePoints;

	public IrregularIntervalSchedule(){

	}
}//end IrregularIntervalSchedule