package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Core.Curve;

/**
 * Default bid curve for default energy bid curve and default startup curves (cost
 * and time).
 * @created 03-Jan-2024 2:08:10 PM
 */
public class DefaultBidCurve extends Curve {

	/**
	 * To indicate a type used for a default energy bid curve, such as LMP, cost or
	 * consultative based.
	 */
	public String curveType;
	/**
	 * Default energy bid adder flag
	 */
	public YesNo debAdderFlag;

	public DefaultBidCurve(){

	}
}//end DefaultBidCurve