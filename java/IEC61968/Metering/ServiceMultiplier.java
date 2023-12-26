package IEC61968.Metering;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Multiplier applied at the usage point.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class ServiceMultiplier extends IdentifiedObject {

	/**
	 * Kind of multiplier.
	 */
	public ServiceMultiplierKind kind;
	/**
	 * Multiplier value.
	 */
	public Float value;

	public ServiceMultiplier(){

	}
}//end ServiceMultiplier