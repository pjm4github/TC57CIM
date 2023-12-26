package IEC61968.Work;


/**
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:26 PM
 */
public enum WorkTaskKind {
	/**
	 * Work task deals with installation of assets.
	 */
	install,
	/**
	 * Work task deals with removal of assets.
	 */
	remove,
	/**
	 * Work task deals with exchange of assets.
	 */
	exchange,
	/**
	 * Work task deals with investigation about assets.
	 */
	investigate
}