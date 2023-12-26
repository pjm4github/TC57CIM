package IEC61968.AssetMeas;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * @author herb
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class StatisticalCalculation extends IdentifiedObject {

	/**
	 * Calculation mode.
	 */
	public CalculationModeKind calculationMode;
	/**
	 * Kind of statistical calculation, specifying how the measurement value is
	 * calculated.
	 */
	public CalculationTechniqueKind calculationTechnique;
	public CalculationMethodOrder CalculationMethodOrder;

	public StatisticalCalculation(){

	}
}//end StatisticalCalculation