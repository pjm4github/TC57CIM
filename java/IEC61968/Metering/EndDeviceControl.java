package IEC61968.Metering;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.FloatQuantity;
import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Instructs an end device (or an end device group) to perform a specified action.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class EndDeviceControl extends IdentifiedObject {

	/**
	 * Level of a demand response program request, where 0=emergency. Note: Attribute
	 * is not defined on DemandResponseProgram as it is not its inherent property (it
	 * serves to control it).
	 */
	public Integer drProgramLevel;
	/**
	 * Whether a demand response program request is mandatory. Note: Attribute is not
	 * defined on DemandResponseProgram as it is not its inherent property (it serves
	 * to control it).
	 */
	public Boolean drProgramMandatory;
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
	 * (if applicable) Price signal used as parameter for this end device control.
	 */
	public FloatQuantity priceSignal;
	/**
	 * Timing for the control actions performed on the device identified in the end
	 * device control.
	 */
	public EndDeviceTiming primaryDeviceTiming;
	/**
	 * Reason for the control action that allows to determine how to continue
	 * processing. For example, disconnect meter command may require different
	 * processing by the receiving system if it has been issued for a network-related
	 * reason (protection) or for a payment-related reason.
	 */
	public String reason;
	/**
	 * (if control has scheduled duration) Date and time interval the control has been
	 * scheduled to execute within.
	 */
	public DateTimeInterval scheduledInterval;
	/**
	 * Timing for the control actions performed by devices that are responding to
	 * event related information sent to the primary device indicated in the end
	 * device control.  For example, load control actions performed by a PAN device in
	 * response to demand response event information sent to a PAN gateway server.
	 */
	public EndDeviceTiming secondaryDeviceTiming;
	/**
	 * All usage point groups receiving commands from this end device control.
	 */
	public UsagePointGroup UsagePointGroups;
	/**
	 * All end devices receiving commands from this end device control.
	 */
	public EndDevice EndDevices;
	/**
	 * End device action issued by this end device control.
	 */
	public EndDeviceAction EndDeviceAction;
	/**
	 * Type of this end device control.
	 */
	public EndDeviceControlType EndDeviceControlType;
	/**
	 * All usage points receiving commands from this end device control.
	 */
	public UsagePoint UsagePoints;

	public EndDeviceControl(){

	}
}//end EndDeviceControl