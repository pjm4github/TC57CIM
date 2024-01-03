package IEC61970.InfIEC61970.InfSIPS;


/**
 * Categorisation of type of compare done on Terminal.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:36:43 PM
 */
public enum PinTerminalKind {
	/**
	 * Active Power on the Terminal.
	 */
	activePower,
	/**
	 * Apparent Power on the Terminal.
	 */
	apparentPower,
	/**
	 * Reactive Power on the Terminal.
	 */
	reactivePower,
	/**
	 * Voltage on the Terminal.
	 */
	voltage
}