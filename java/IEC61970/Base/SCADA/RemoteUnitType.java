package IEC61970.Base.SCADA;


/**
 * Type of remote unit.
 * @created 02-Jan-2024 11:30:39 PM
 */
public enum RemoteUnitType {
	/**
	 * Remote terminal unit.
	 */
	RTU,
	/**
	 * Substation control system.
	 */
	SubstationControlSystem,
	/**
	 * Control center.
	 */
	ControlCenter,
	/**
	 * Intelligent electronic device (IED).
	 */
	IED
}