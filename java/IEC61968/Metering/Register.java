package IEC61968.Metering;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.TimeInterval;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A device that indicates or records units of the commodity or other quantity
 * measured.
 * @created 25-Dec-2023 8:45:24 PM
 */
public class Register extends IdentifiedObject {

	/**
	 * If true, the data it produces is  calculated or measured by a device other than
	 * a physical end device/meter. Otherwise, any data streams it produces are
	 * measured by the hardware of the end device/meter itself. 
	 */
	public Boolean isVirtual;
	/**
	 * Number of digits (dials on a mechanical meter) to the left of the decimal place;
	 * default is normally 5.
	 */
	public Integer leftDigitCount;
	/**
	 * Number of digits (dials on a mechanical meter) to the right of the decimal
	 * place.
	 */
	public Integer rightDigitCount;
	/**
	 * Clock time interval for register to beging/cease accumulating time of usage (e.
	 * g., start at 8:00 am, stop at 5:00 pm).
	 */
	public TimeInterval touTier;
	/**
	 * Name used for the time of use tier (also known as bin or bucket).  For example,
	 * "peak", "off-peak", "TOU Category A", etc. 
	 */
	public String touTierName;
	/**
	 * All channels that collect/report values from this register.
	 */
	public Channel Channels;
	/**
	 * End device function metering quantities displayed by this register.
	 */
	public EndDeviceFunction EndDeviceFunction;

	public Register(){

	}
}//end Register