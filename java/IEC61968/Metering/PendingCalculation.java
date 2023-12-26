package IEC61968.Metering;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Float;

/**
 * When present, a scalar conversion that needs to be applied to every
 * IntervalReading.value contained in IntervalBlock. This conversion results in a
 * new associated ReadingType, reflecting the true dimensions of IntervalReading
 * values after the conversion.
 * @created 25-Dec-2023 8:45:23 PM
 */
public class PendingCalculation {

	/**
	 * Whether scalars should be applied before adding the 'offset'.
	 */
	public Boolean multiplyBeforeAdd;
	/**
	 * (if applicable) Offset to be added as well as multiplication using scalars.
	 */
	public Integer offset;
	/**
	 * (if scalar is rational number) When 'IntervalReading.value' is multiplied by
	 * 'scalarNumerator' and divided by this value, it causes a unit of measure
	 * conversion to occur, resulting in the 'ReadingType.unit'.
	 */
	public Integer scalarDenominator;
	/**
	 * (if scalar is floating number) When multiplied with 'IntervalReading.value', it
	 * causes a unit of measure conversion to occur, according to the 'ReadingType.
	 * unit'.
	 */
	public Float scalarFloat;
	/**
	 * (if scalar is integer or rational number)  When the scalar is a simple integer,
	 * and this attribute is presented alone and multiplied with 'IntervalReading.
	 * value', it causes a unit of measure conversion to occur, resulting in the
	 * 'ReadingType.unit'. It is never used in conjunction with 'scalarFloat', only
	 * with 'scalarDenominator'.
	 */
	public Integer scalarNumerator;
	/**
	 * Reading type resulting from this pending conversion.
	 */
	public ReadingType ReadingType;

	public PendingCalculation(){

	}
}//end PendingCalculation