package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.Money;

/**
 * Details on amounts due for an account.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:21 PM
 */
public class Due {

	/**
	 * Part of 'current' that constitutes the arrears portion.
	 */
	public Money arrears;
	/**
	 * Part of 'current' that constitutes the charge portion: 'charges' = 'Charge.
	 * fixedPortion' + 'Charge.variablePortion'.
	 */
	public Money charges;
	/**
	 * Current total amount now due: current = principle + arrears + interest +
	 * charges. Typically the rule for settlement priority is: interest dues, then
	 * arrears dues, then current dues, then charge dues.
	 */
	public Money current;
	/**
	 * Part of 'current' that constitutes the interest portion.
	 */
	public Money interest;
	/**
	 * Part of 'current' that constitutes the portion of the principle amount
	 * currently due.
	 */
	public Money principle;

	public Due(){

	}
}//end Due