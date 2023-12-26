package IEC61968.Metering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Minutes;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.DateTime;

/**
 * Action/command performed by an end device on a device other than the end device.
 * 
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:21 PM
 */
public class EndDeviceAction {

	/**
	 * Command text.
	 */
	public String command;
	/**
	 * Amount of time the action of this control is to remain active.
	 */
	public Minutes duration;
	/**
	 * True if the action of this control is indefinite.
	 */
	public Boolean durationIndefinite;
	/**
	 * Start date and time for action of this control.
	 */
	public DateTime startDateTime;

	public EndDeviceAction(){

	}
}//end EndDeviceAction