package IEC61970.Dynamics.StandardModels.WindDynamics;


/**
 * UVRT Q control modes <i>M</i><sub>qUVRT</sub>.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public enum WindUVRTQcontrolModeKind {
	/**
	 * Voltage dependent reactive current injection
	 * (<i>M</i><i><sub>q</sub></i><sub>UVRT </sub>equals 0).
	 */
	mode0,
	/**
	 * Reactive current injection controlled as the pre-fault value plus an additional
	 * voltage dependent reactive current injection
	 * (<i>M</i><i><sub>q</sub></i><sub>UVRT</sub> equals 1).
	 */
	mode1,
	/**
	 * Reactive current injection controlled as the pre-fault value plus an additional
	 * voltage dependent reactive current injection during fault, and as the pre-fault
	 * value plus an additional constant reactive current injection post fault
	 * (<i>M</i><i><sub>q</sub></i><sub>UVRT </sub>equals 2).
	 */
	mode2
}