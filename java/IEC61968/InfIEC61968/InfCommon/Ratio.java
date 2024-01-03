package IEC61968.InfIEC61968.InfCommon;

import IEC61970.Base.Domain.Float;

/**
 * Fraction specified explicitly with a numerator and denominator, which can be
 * used to calculate the quotient.
 * @created 29-Dec-2023 6:02:59 PM
 */
public class Ratio {

	/**
	 * The part of a fraction that is below the line and that functions as the divisor
	 * of the numerator.
	 */
	public Float denominator;
	/**
	 * The part of a fraction that is above the line and signifies the number to be
	 * divided by the denominator.
	 */
	public Float numerator;

	public Ratio(){

	}
}//end Ratio