package IEC61968.Assets;


/**
 * Kind of seal condition.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public enum SealConditionKind {
	/**
	 * Seal is locked.
	 */
	locked,
	/**
	 * Seal is open.
	 */
	open,
	/**
	 * Seal is broken.
	 */
	broken,
	/**
	 * Seal is missing.
	 */
	missing,
	/**
	 * Other kind of seal condition.
	 */
	other
}