package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.ParticipantInterfaces.BidSelfSched;

/**
 * Groups Adjacent Control Areas.
 * @created 03-Jan-2024 2:15:33 PM
 */
public class AdjacentCASet extends IdentifiedObject {

	/**
	 * Loss percentage
	 */
	public Float lossPercentage ;
	public SubControlArea SubControlArea;
	public BidSelfSched BidSelfSched;

	public AdjacentCASet(){

	}
}//end AdjacentCASet