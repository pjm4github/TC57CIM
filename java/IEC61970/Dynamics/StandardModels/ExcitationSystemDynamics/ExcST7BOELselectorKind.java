package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;


/**
 * Type of connection for the OEL input used for static excitation systems type 7B.
 * 
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public enum ExcST7BOELselectorKind {
	/**
	 * No OEL input is used.
	 */
	noOELinput,
	/**
	 * The signal is added to Vref.
	 */
	addVref,
	/**
	 * The signal is connected in the input of the LV gate.
	 */
	inputLVgate,
	/**
	 * The signal is connected in the output of the LV gate.
	 */
	outputLVgate
}