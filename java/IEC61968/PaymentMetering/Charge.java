package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A charge element associated with other entities such as tariff structures,
 * auxiliary agreements or other charge elements. The total charge amount
 * applicable to this instance of charge is the sum of fixed and variable portion.
 * @created 25-Dec-2023 8:45:20 PM
 */
public class Charge extends IdentifiedObject {

	/**
	 * The fixed portion of this charge element.
	 */
	public AccountingUnit fixedPortion;
	/**
	 * The kind of charge to be applied.
	 */
	public ChargeKind kind;
	/**
	 * The variable portion of this charge element, calculated as a percentage of the
	 * total amount of a parent charge.
	 */
	public PerCent variablePortion;
	/**
	 * All sub-components of this complex charge.
	 */
	public Charge ChildCharges;

	public Charge(){

	}
}//end Charge