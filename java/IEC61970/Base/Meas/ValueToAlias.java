package IEC61970.Base.Meas;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Describes the translation of one particular value into a name, e.g. 1 as "Open".
 * 
 * @created 02-Jan-2024 11:26:48 PM
 */
public class ValueToAlias extends IdentifiedObject {

	/**
	 * The value that is mapped.
	 */
	public Integer value;

	public ValueToAlias(){

	}
}//end ValueToAlias