package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;


/**
 * Governor control flag for Francis hydro model.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public enum FrancisGovernorControlKind {
	/**
	 * Mechanic-hydraulic regulator with tacho-accelerometer (Cflag = 1).
	 */
	mechanicHydrolicTachoAccelerator,
	/**
	 * Mechanic-hydraulic regulator with transient feedback (Cflag=2).
	 */
	mechanicHydraulicTransientFeedback,
	/**
	 * Electromechanical and electrohydraulic regulator (Cflag=3).
	 */
	electromechanicalElectrohydraulic
}