package IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics;


/**
 * Excitation base system mode.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public enum IfdBaseKind {
	/**
	 * Air gap line mode.  ifdBaseValue is computed, not defined by the user, in this
	 * mode.
	 */
	ifag,
	/**
	 * No load system with saturation mode.  ifdBaseValue is computed, not defined by
	 * the user, in this mode.
	 */
	ifnl,
	/**
	 * Full load system mode.  ifdBaseValue is computed, not defined by the user, in
	 * this mode.
	 */
	iffl
}