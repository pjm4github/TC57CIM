package IEC61970.Dynamics.StandardModels.WindDynamics;


/**
 * General wind turbine Q control modes <i>M</i><sub>qG</sub>.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public enum WindQcontrolModeKind {
	/**
	 * Voltage control (<i>M</i><i><sub>q</sub></i><sub>G</sub> equals 0).
	 */
	voltage,
	/**
	 * Reactive power control (<i>M</i><i><sub>q</sub></i><sub>G</sub> equals 1).
	 */
	reactivePower,
	/**
	 * Open loop reactive power control (only used with closed loop at plant level)
	 * (<i>M</i><i><sub>q</sub></i><sub>G </sub>equals 2).
	 */
	openLoopReactivePower,
	/**
	 * Power factor control (<i>M</i><i><sub>q</sub></i><sub>G </sub>equals 3).
	 */
	powerFactor,
	/**
	 * Open loop power factor control (<i>M</i><i><sub>q</sub></i><sub>G </sub>equals
	 * 4).
	 */
	openLooppowerFactor
}