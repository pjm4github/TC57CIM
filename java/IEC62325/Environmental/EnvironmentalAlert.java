package IEC62325.Environmental;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.DateTimeInterval;
import IEC61968.Common.ActivityRecord;

/**
 * An environmental alert issued by a provider or system.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class EnvironmentalAlert extends ActivityRecord {

	/**
	 * The type of the issued alert which is drawn from the specified alert type list. 
	 */
	public String alertType;
	/**
	 * Time and date alert cancelled. Used only if alert is cancelled before it
	 * expires.
	 */
	public DateTime cancelledDateTime;
	/**
	 * An abbreviated textual description of the alert issued.
	 * Note: the full text of the alert appears in the .description attribute
	 * (inherited from IdentifiedObject).
	 */
	public String headline;
	/**
	 * The interval for which this weather alert is in effect.
	 */
	public DateTimeInterval inEffect;
	/**
	 * Environmental data provider for this alert.
	 */
	public EnvironmentalDataProvider EnvironmentalDataProvider;
	/**
	 * The list of alert types from which the type of this alert is drawn.
	 */
	public AlertTypeList AlertTypeList;
	/**
	 * Type of location to which this environmental alert applies.
	 */
	public EnvironmentalLocationType EnvironmentalLocationKind;

	public EnvironmentalAlert(){

	}
}//end EnvironmentalAlert