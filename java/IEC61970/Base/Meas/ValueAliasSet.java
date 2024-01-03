package IEC61970.Base.Meas;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * Describes the translation of a set of values into a name and is intendend to
 * facilitate cusom translations. Each ValueAliasSet has a name, description etc.
 * A specific Measurement may represent a discrete state like Open, Closed,
 * Intermediate etc. This requires a translation from the MeasurementValue.value
 * number to a string, e.g. 0->"Invalid", 1->"Open", 2->"Closed", 3-
 * >"Intermediate". Each ValueToAlias member in ValueAliasSet.Value describe a
 * mapping for one particular value to a name.
 * @created 02-Jan-2024 11:26:26 PM
 */
public class ValueAliasSet extends IdentifiedObject {

	/**
	 * The ValueToAlias mappings included in the set.
	 */
	public ValueToAlias Values;
	/**
	 * The Measurements using the set for translation.
	 */
	public Discrete Discretes;

	public ValueAliasSet(){

	}
}//end ValueAliasSet