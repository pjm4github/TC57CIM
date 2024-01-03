package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC62325.MarketOperations.MktDomain.BidCalculationBasis;
import IEC61970.Base.Core.CurveData;

/**
 * Curve data for default bid curve and startup cost curve.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class DefaultBidCurveData extends CurveData {

	/**
	 * Type of calculation basis used to define the default bid segment curve.
	 */
	public BidCalculationBasis bidSegmentCalcType;

	public DefaultBidCurveData(){

	}
}//end DefaultBidCurveData