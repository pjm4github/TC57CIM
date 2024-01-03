package IEC61970.Base.Core;

import IEC61970.Base.Meas.Control;
import IEC61970.Base.Meas.Measurement;
import IEC61968.Common.ConfigurationEvent;

/**
 * A power system resource can be an item of equipment such as a switch, an
 * equipment container containing many individual items of equipment such as a
 * substation, or an organisational entity such as sub-control area. Power system
 * resources can have measurements associated.
 * @created 02-Jan-2024 10:36:22 PM
 */
public class PowerSystemResource extends IdentifiedObject {

	/**
	 * The controller outputs used to actually govern a regulating device, e.g. the
	 * magnetization of a synchronous machine or capacitor bank breaker actuator.
	 */
	public Control Controls;
	/**
	 * The measurements associated with this power system resource.
	 */
	public Measurement Measurements;
	/**
	 * Custom classification for this power system resource.
	 */
	public PSRType PSRType;
	public ConfigurationEvent ConfigurationEvent;

	public PowerSystemResource(){

	}
}//end PowerSystemResource