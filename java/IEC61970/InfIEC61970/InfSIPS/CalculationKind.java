package IEC61970.InfIEC61970.InfSIPS;


/**
 * Categorisation of calculation operation that can be done to Measurement.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:35:47 PM
 */
public enum CalculationKind {
	/**
	 * Summation operation over the input values (operands).
	 */
	sum,
	/**
	 * Multiplication operation the input values (operands).
	 */
	mul,
	/**
	 * Division operation the input values (operands).
	 */
	div,
	/**
	 * Square root operator - only one input value (operands).
	 */
	sqrt
}