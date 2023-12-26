package IEC61968.Assets;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Duration;
import IEC61970.Base.Domain.DateTime;
import IEC61968.Common.ActivityRecord;

/**
 * An asset health-related event that is created by an analytic. The event is a
 * record of a change in asset health.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public class AssetHealthEvent extends ActivityRecord {

	/**
	 * Recommendation for action.
	 */
	public String actionRecommendation;
	/**
	 * Time horizon for action.
	 */
	public Duration actionTimeline;
	/**
	 * The date and time when the event is effective.
	 */
	public DateTime effectiveDateTime;

	public AssetHealthEvent(){

	}
}//end AssetHealthEvent