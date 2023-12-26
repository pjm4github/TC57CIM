package IEC61970.Base.Wires;


/**
 * The kind of regulation model.   For example regulating voltage, reactive power,
 * active power, etc.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public enum RegulatingControlModeKind {
	/**
	 * Voltage is specified.
	 */
	voltage,
	/**
	 * Active power is specified.
	 */
	activePower,
	/**
	 * Reactive power is specified.
	 */
	reactivePower,
	/**
	 * Current flow is specified.
	 */
	currentFlow,
	/**
	 * Admittance is specified.
	 */
	admittance,
	/**
	 * Control switches on/off by time of day. The times may change on the weekend, or
	 * in different seasons.
	 */
	timeScheduled,
	/**
	 * Control switches on/off based on the local temperature (i.e., a thermostat).
	 */
	temperature,
	/**
	 * Power factor is specified.
	 */
	powerFactor
}