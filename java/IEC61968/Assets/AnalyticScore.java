package IEC61968.Assets;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * An indicative scoring by an analytic that can be used to characterize the
 * health of or the risk associated with one or more assets.  The analytic score
 * reflects the results of an execution of an analytic against an asset or group
 * of assets.
 * @author Gowri
 * @version 1.0
 * @created 07-Jan-2024 9:45:09 PM
 */
public class AnalyticScore extends IdentifiedObject {

	/**
	 * Timestamp of when the score was calculated.
	 */
	public DateTime calculationDateTime;
	/**
	 * Date-time for when the score applies.
	 */
	public DateTime effectiveDateTime;
	/**
	 * Asset health score value.
	 */
	public Float value;
	public Asset Asset;

	public AnalyticScore(){

	}
}//end AnalyticScore