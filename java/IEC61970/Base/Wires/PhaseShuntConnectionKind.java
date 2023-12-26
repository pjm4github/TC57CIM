package IEC61970.Base.Wires;


/**
 * The configuration of phase connections for a single terminal device such as a
 * load or capacitor.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public enum PhaseShuntConnectionKind {
	/**
	 * Delta connection.
	 */
	D,
	/**
	 * Wye connection.
	 */
	Y,
	/**
	 * Wye, with neutral brought out for grounding.
	 */
	Yn,
	/**
	 * Independent winding, for single-phase connections.
	 */
	I,
	/**
	 * Ground connection; use when explicit connection to ground needs to be expressed
	 * in combination with the phase code, such as for electrical wire/cable or for
	 * meters.
	 */
	G
}