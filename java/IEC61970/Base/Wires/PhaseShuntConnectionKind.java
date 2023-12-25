package TC57CIM.IEC61970.Base.Wires;


/**
 * The configuration of phase connections for a single terminal device such as a
 * load or capacitor.
 * @author kdemaree
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
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