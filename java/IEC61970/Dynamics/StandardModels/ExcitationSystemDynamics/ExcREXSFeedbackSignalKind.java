package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;


/**
 * Type of rate feedback signals.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public enum ExcREXSFeedbackSignalKind {
	/**
	 * The voltage regulator output voltage is used. It is the same as exciter field
	 * voltage.
	 */
	fieldVoltage,
	/**
	 * The exciter field current is used.
	 */
	fieldCurrent,
	/**
	 * The output voltage of the exciter is used.
	 */
	outputVoltage
}