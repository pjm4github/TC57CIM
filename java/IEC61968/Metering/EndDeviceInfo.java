package IEC61968.Metering;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.Voltage;
import IEC61968.Assets.AssetInfo;

/**
 * End device data.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class EndDeviceInfo extends AssetInfo {

	/**
	 * Inherent capabilities of the device (i.e., the functions it supports).
	 */
	public EndDeviceCapability capability;
	/**
	 * If true, this is a solid state end device (as opposed to a mechanical or
	 * electromechanical device).
	 */
	public Boolean isSolidState;
	/**
	 * Number of potential phases the end device supports, typically 0, 1 or 3.
	 */
	public Integer phaseCount;
	/**
	 * Rated current.
	 */
	public CurrentFlow ratedCurrent;
	/**
	 * Rated voltage.
	 */
	public Voltage ratedVoltage;

	public EndDeviceInfo(){

	}
}//end EndDeviceInfo