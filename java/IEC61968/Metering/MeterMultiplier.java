package IEC61968.Metering;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Multiplier applied at the meter.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class MeterMultiplier extends IdentifiedObject {

	/**
	 * Kind of multiplier.
	 */
	public MeterMultiplierKind kind;
	/**
	 * Multiplier value.
	 */
	public Float value;

	public MeterMultiplier(){

	}
}//end MeterMultiplier