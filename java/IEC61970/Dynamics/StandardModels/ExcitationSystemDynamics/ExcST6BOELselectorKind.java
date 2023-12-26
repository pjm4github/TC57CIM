package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;


/**
 * Type of connection for the OEL input used for static excitation systems type 6B.
 * 
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public enum ExcST6BOELselectorKind {
	/**
	 * No OEL input is used.
	 */
	noOELinput,
	/**
	 * The connection is before UEL.
	 */
	beforeUEL,
	/**
	 * The connection is after UEL.
	 */
	afterUEL
}