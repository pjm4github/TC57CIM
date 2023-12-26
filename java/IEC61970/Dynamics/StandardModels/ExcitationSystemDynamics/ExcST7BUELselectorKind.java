package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;


/**
 * Type of connection for the UEL input used for static excitation systems type 7B.
 * 
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public enum ExcST7BUELselectorKind {
	/**
	 * No UEL input is used.
	 */
	noUELinput,
	/**
	 * The signal is added to Vref.
	 */
	addVref,
	/**
	 * The signal is connected in the input of the HV gate.
	 */
	inputHVgate,
	/**
	 * The signal is connected in the output of the HV gate.
	 */
	outputHVgate
}