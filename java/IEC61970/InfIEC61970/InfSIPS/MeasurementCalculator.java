package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * Result of a calculation of one or more measurement.
 * @author sveinols
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class MeasurementCalculator extends IdentifiedObject {

	/**
	 * Calculation operation executed on the operants.
	 */
	public CalculationKind kind;
	public PinMeasurement PinMeasurement;
	public MeasurementCalculatorInput MeasurementCalculatorInput;

	public MeasurementCalculator(){

	}
}//end MeasurementCalculator