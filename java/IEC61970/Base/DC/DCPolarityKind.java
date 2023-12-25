package TC57CIM.IEC61970.Base.DC;


/**
 * Polarity for DC circuits.
 * @author T. Kostic
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public enum DCPolarityKind {
	/**
	 * Positive pole.
	 */
	positive,
	/**
	 * Middle pole, potentially grounded.
	 */
	middle,
	/**
	 * Negative pole.
	 */
	negative
}