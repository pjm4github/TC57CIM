package IEC61970.Base.SCADA;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Meas.Control;

/**
 * Remote controls are ouputs that are sent by the remote unit to actuators in the
 * process.
 * @created 02-Jan-2024 11:28:57 PM
 */
public class RemoteControl extends RemotePoint {

	/**
	 * The maximum set point value accepted by the remote control point.
	 */
	public Float actuatorMaximum;
	/**
	 * The minimum set point value accepted by the remote control point.
	 */
	public Float actuatorMinimum;
	/**
	 * Set to true if the actuator is remotely controlled.
	 */
	public Boolean remoteControlled;
	/**
	 * The Control for the RemoteControl point.
	 */
	public Control Control;

	public RemoteControl(){

	}
}//end RemoteControl