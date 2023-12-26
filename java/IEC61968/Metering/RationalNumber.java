package IEC61968.Metering;

import IEC61970.Base.Domain.Integer;

/**
 * Rational number = 'numerator' / 'denominator'.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class RationalNumber {

	/**
	 * Denominator. Value 1 indicates the number is a simple integer.
	 */
	public Integer denominator;
	/**
	 * Numerator.
	 */
	public Integer numerator;

	public RationalNumber(){

	}
}//end RationalNumber