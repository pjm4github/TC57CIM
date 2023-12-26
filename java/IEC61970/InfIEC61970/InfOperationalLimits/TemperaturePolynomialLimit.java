package IEC61970.InfIEC61970.InfOperationalLimits;

import IEC61970.Base.Domain.Float;

/**
 * This describes the coefficients of a polynomial function that has temperature
 * as input and calculates limit values as output.
 * @author akamath
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class TemperaturePolynomialLimit extends EnvironmentalDependentLimit {

	/**
	 * The polinomial coefficent of power 0.
	 */
	public Float coefficient0;
	/**
	 * The polinomial coefficent of power 1.
	 */
	public Float coefficient1;
	/**
	 * The polinomial coefficent of power 2.
	 */
	public Float coefficient2;
	/**
	 * The polinomial coefficent of power 3.
	 */
	public Float coefficient3;
	/**
	 * The polinomial coefficent of power 4.
	 */
	public Float coefficient4;

	public TemperaturePolynomialLimit(){

	}
}//end TemperaturePolynomialLimit