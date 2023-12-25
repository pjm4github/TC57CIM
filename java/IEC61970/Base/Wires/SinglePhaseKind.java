package TC57CIM.IEC61970.Base.Wires;


/**
 * Enumeration of single phase identifiers. Allows designation of single phases
 * for both transmission and distribution equipment, circuits and loads.
 * @author T. Kostic
 * @version 1.0
 * @created 15-Dec-2023 4:38:29 PM
 */
public enum SinglePhaseKind {
	/**
	 * Phase A.
	 */
	A,
	/**
	 * Phase B.
	 */
	B,
	/**
	 * Phase C.
	 */
	C,
	/**
	 * Neutral.
	 */
	N,
	/**
	 * Secondary phase 1.
	 */
	s1,
	/**
	 * Secondary phase 2.
	 */
	s2
}