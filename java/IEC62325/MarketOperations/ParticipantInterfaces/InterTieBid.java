package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.Integer;
import IEC62325.MarketOperations.ReferenceData.RegisteredInterTie;

/**
 * This class represents the inter tie bid.
 * @created 28-Dec-2023 5:21:28 PM
 */
public class InterTieBid extends ResourceBid {

	/**
	 * The minimum hourly block for an Inter-Tie Resource supplied within the bid.
	 */
	public Integer minHourlyBlock ;
	public RegisteredInterTie RegisteredInterTie;
	public RampRateCurve RampRateCurve;

	public InterTieBid(){

	}
}//end InterTieBid