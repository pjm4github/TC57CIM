package IEC61968.Metering;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;

/**
 * PAN action/command used to issue the displaying of text messages on PAN devices.
 * 
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class PanDisplay extends EndDeviceAction {

	/**
	 * If true, the requesting entity (e.g. retail electric provider) requires
	 * confirmation of the successful display of the text message.
	 */
	public Boolean confirmationRequired;
	/**
	 * Priority associated with the text message to be displayed.
	 */
	public String priority;
	/**
	 * Text to be displayed by a PAN device.
	 */
	public String textMessage;
	/**
	 * Transmission mode to be used for this PAN display control.
	 */
	public TransmissionModeKind transmissionMode;

	public PanDisplay(){

	}
}//end PanDisplay