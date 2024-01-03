package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.ReserveRequirementType;
import IEC61970.Base.Core.Curve;

/**
 * Reserve demand curve.  Models maximum quantities of reserve required per Market
 * Region and models a reserve demand curve for the minimum quantities of reserve.
 * The ReserveDemandCurve is a relationship between unit operating reserve price
 * in $/MWhr (Y-axis) and unit reserves in MW (X-axis).
 * @created 03-Jan-2024 2:08:11 PM
 */
public class ReserveDemandCurve extends Curve {

	/**
	 * Region requirement maximum limit
	 */
	public Float reqMaxMW;
	/**
	 * Reserve requirement type that the max and curve apply to. For example,
	 * operating reserve, regulation and contingency.
	 */
	public ReserveRequirementType reserveRequirementType;

	public ReserveDemandCurve(){

	}
}//end ReserveDemandCurve