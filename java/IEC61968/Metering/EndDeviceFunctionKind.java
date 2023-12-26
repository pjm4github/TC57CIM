package IEC61968.Metering;


/**
 * Kind of end device function.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:21 PM
 */
public enum EndDeviceFunctionKind {
	/**
	 * Detection and monitoring of reverse flow.
	 */
	reverseFlow,
	/**
	 * Demand response functions.
	 */
	demandResponse,
	/**
	 * Presentation of metered values to a user or another system (always a function
	 * of a meter, but might not be supported by a load control unit).
	 */
	metrology,
	/**
	 * Reporting historical power interruption data.
	 */
	outageHistory,
	/**
	 * Support for one or more relays that may be programmable in the meter (and tied
	 * to TOU, time pulse, load control or other functions).
	 */
	relaysProgramming,
	/**
	 * On-request reads.
	 */
	onRequestRead,
	/**
	 * Autonomous application of daylight saving time (DST).
	 */
	autonomousDst,
	/**
	 * Electricity metering.
	 */
	electricMetering,
	/**
	 * Gas metering.
	 */
	gasMetering,
	/**
	 * Water metering.
	 */
	waterMetering
}