package IEC61968.AssetMeas;

import IEC61970.Base.Domain.Integer;

/**
 * Description of period for which calculation is performed.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class PeriodicStatisticalCalculation extends StatisticalCalculation {

	/**
	 * Number of units (of calculationIntervalUnit) in the calculation interval.
	 */
	public Integer calculationIntervalMagnitude;
	/**
	 * Unit in which calculation interval is defined.
	 */
	public CalculationIntervalUnitKind calculationIntervalUnit;

	public PeriodicStatisticalCalculation(){

	}
}//end PeriodicStatisticalCalculation