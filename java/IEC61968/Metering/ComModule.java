package IEC61968.Metering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Minutes;
import IEC61968.Assets.Asset;

/**
 * An asset having communications capabilities that can be paired with a meter or
 * other end device to provide the device with communication ability, through
 * associated communication function. An end device that has communications
 * capabilities through embedded hardware can use that function directly (without
 * the communication module), or combine embedded communication function with
 * additional communication functions provided through an external communication
 * module (e.g. zigbee).
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class ComModule extends Asset {

	/**
	 * Automated meter reading (AMR) system communicating with this com module.
	 */
	public String amrSystem;
	/**
	 * If true, autonomous daylight saving time (DST) function is supported.
	 */
	public Boolean supportsAutonomousDst;
	/**
	 * Time zone offset relative to GMT for the location of this com module.
	 */
	public Minutes timeZoneOffset;
	/**
	 * All functions this communication module performs.
	 */
	public ComFunction ComFunctions;

	public ComModule(){

	}
}//end ComModule