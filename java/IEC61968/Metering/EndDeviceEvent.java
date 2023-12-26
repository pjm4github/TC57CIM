package IEC61968.Metering;

import IEC61970.Base.Domain.String;
import IEC61968.Common.ActivityRecord;

/**
 * Event detected by a device function associated with the end device.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class EndDeviceEvent extends ActivityRecord {

	/**
	 * Unique identifier of the business entity originating an end device control.
	 */
	public String issuerID;
	/**
	 * Identifier assigned by the initiator (e.g. retail electric provider) of an end
	 * device control action to uniquely identify the demand response event, text
	 * message, or other subject of the control action. Can be used when cancelling an
	 * event or text message request or to identify the originating event or text
	 * message in a consequential end device event.
	 */
	public String issuerTrackingID;
	/**
	 * (if user initiated) ID of user who initiated this end device event.
	 */
	public String userID;
	/**
	 * Type of this end device event.
	 */
	public EndDeviceEventType EndDeviceEventType;
	/**
	 * All details of this end device event.
	 */
	public EndDeviceEventDetail EndDeviceEventDetails;
	/**
	 * End device that reported this end device event.
	 */
	public EndDevice EndDevice;
	/**
	 * Usage point for which this end device event is reported.
	 */
	public UsagePoint UsagePoint;

	public EndDeviceEvent(){

	}
}//end EndDeviceEvent