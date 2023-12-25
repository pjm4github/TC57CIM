


/**
 * Winding connection type.
 * @author pmora
 * @updated 15-Dec-2023 1:39:42 PM
 */
public enum WindingConnection {
	/**
	 * Delta
	 */
	D,
	/**
	 * Wye
	 */
	Y,
	/**
	 * ZigZag
	 */
	Z,
	/**
	 * Wye, with neutral brought out for grounding.
	 */
	Yn,
	/**
	 * ZigZag, with neutral brought out for grounding.
	 */
	Zn,
	/**
	 * Autotransformer common winding
	 */
	A,
	/**
	 * Independent winding, for single-phase connections
	 */
	I
}