package IEC61968.Metering;

import IEC61970.Base.Domain.Boolean;

/**
 * Inherent capabilities of an end device (i.e., the functions it supports).
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:21 PM
 */
public class EndDeviceCapability {

	/**
	 * True if autonomous DST (daylight saving time) function is supported.
	 */
	public Boolean autonomousDst;
	/**
	 * True if communication function is supported.
	 */
	public Boolean communication;
	/**
	 * True if connect and disconnect function is supported.
	 */
	public Boolean connectDisconnect;
	/**
	 * True if demand response function is supported.
	 */
	public Boolean demandResponse;
	/**
	 * True if electric metering function is supported.
	 */
	public Boolean electricMetering;
	/**
	 * True if gas metering function is supported.
	 */
	public Boolean gasMetering;
	/**
	 * True if metrology function is supported.
	 */
	public Boolean metrology;
	/**
	 * True if on request read function is supported.
	 */
	public Boolean onRequestRead;
	/**
	 * True if outage history function is supported.
	 */
	public Boolean outageHistory;
	/**
	 * True if device performs pressure compensation for metered quantities.
	 */
	public Boolean pressureCompensation;
	/**
	 * True if pricing information is supported.
	 */
	public Boolean pricingInfo;
	/**
	 * True if device produces pulse outputs.
	 */
	public Boolean pulseOutput;
	/**
	 * True if relays programming function is supported.
	 */
	public Boolean relaysProgramming;
	/**
	 * True if reverse flow function is supported.
	 */
	public Boolean reverseFlow;
	/**
	 * True if device performs super compressibility compensation for metered
	 * quantities.
	 */
	public Boolean superCompressibilityCompensation;
	/**
	 * True if device performs temperature compensation for metered quantities.
	 */
	public Boolean temperatureCompensation;
	/**
	 * True if the displaying of text messages is supported.
	 */
	public Boolean textMessage;
	/**
	 * True if water metering function is supported.
	 */
	public Boolean waterMetering;

	public EndDeviceCapability(){

	}
}//end EndDeviceCapability