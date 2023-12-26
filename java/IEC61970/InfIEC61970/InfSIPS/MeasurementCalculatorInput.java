package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Meas.Measurement;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Input to measurement calculation.  Support Analog, Discrete and Accumulator.
 * @author sveinols
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class MeasurementCalculatorInput extends IdentifiedObject {

	/**
	 * If true, use the absolute value for the calculation. 
	 */
	public Boolean absoluteValue;
	/**
	 * Positive number that defines the order of the operant in the calculation. 0 =
	 * default. The order is not relevant (e.g. summation). 
	 */
	public Integer order;
	public Measurement Measurement;

	public MeasurementCalculatorInput(){

	}
}//end MeasurementCalculatorInput