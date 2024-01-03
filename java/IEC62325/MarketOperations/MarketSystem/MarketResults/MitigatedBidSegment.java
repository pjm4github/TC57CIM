package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.String;

/**
 * Model of mitigated bid. Indicates segment of piece-wise linear bid, that has
 * been mitigated.
 * @created 28-Dec-2023 8:23:55 PM
 */
public class MitigatedBidSegment {

	public DateTime intervalStartTime;
	/**
	 * Mitigated bid segment MW value
	 */
	public Float segmentMW;
	/**
	 * Mitigated Bid Segment Number
	 */
	public Integer segmentNumber;
	public String thresholdType;

	public MitigatedBidSegment(){

	}
}//end MitigatedBidSegment