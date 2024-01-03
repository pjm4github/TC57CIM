package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Core.Curve;

/**
 * Relationship between unit operating price in $/hour (Y-axis) and unit output in
 * MW (X-axis).
 * @created 28-Dec-2023 5:19:23 PM
 */
public class BidPriceCurve extends Curve {

	public BidPriceSchedule BidSchedule;

	public BidPriceCurve(){

	}
}//end BidPriceCurve