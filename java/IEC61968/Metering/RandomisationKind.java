package IEC61968.Metering;


/**
 * Kind of randomisation to be applied to control the timing of end device control
 * commands and/or the definition of demand response and load control events.
 * Value other than 'none' is typically used to mitigate potential deleterious
 * effects of simultaneous operation of multiple devices.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public enum RandomisationKind {
	/**
	 * Start time of an event or control action affecting one or more multiple devices
	 * is randomised.
	 */
	start,
	/**
	 * End time of an event or control action affecting one or more devices is
	 * randomised to prevent simultaneous operation.
	 */
	end,
	/**
	 * Both the start time and the end time of an event or control action affecting
	 * one or more devices are randomised to prevent simultaneous operation.
	 */
	startAndEnd,
	/**
	 * Randomisation of start and/or end times involving the operation of one or more
	 * devices is controlled by default settings for the device(s).
	 */
	default,
	/**
	 * Neither the start time nor the end time of an event or control action affecting
	 * one or more devices is randomised.
	 */
	none
}