package IEC61970.Base.DC;


/**
 * Polarity for DC circuits.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
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