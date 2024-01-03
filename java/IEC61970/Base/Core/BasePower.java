package IEC61970.Base.Core;

import IEC61970.Base.Domain.ApparentPower;

/**
 * The BasePower class defines the base power used in the per unit calculations.
 * @created 02-Jan-2024 10:16:14 PM
 */
public class BasePower extends IdentifiedObject {

	/**
	 * Value used as base power.
	 */
	public ApparentPower basePower;

	public BasePower(){

	}
}//end BasePower