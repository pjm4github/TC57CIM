package IEC61970.Dynamics.StandardModels.WindDynamics;


/**
 * Reactive power/voltage controller mode.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public enum WindPlantQcontrolModeKind {
	/**
	 * Reactive power reference.
	 */
	reactivePower,
	/**
	 * Power factor reference.
	 */
	powerFactor,
	/**
	 * UQ static.
	 */
	uqStatic,
	/**
	 * Voltage control.
	 */
	voltageControl
}