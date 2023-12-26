package IEC61968.Work;


/**
 * Kind of work.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:26 PM
 */
public enum WorkKind {
	/**
	 * Construction work.
	 */
	construction,
	/**
	 * Inspection work.
	 */
	inspection,
	/**
	 * Maintenance work.
	 */
	maintenance,
	/**
	 * Repair work.
	 */
	repair,
	/**
	 * Test work.
	 */
	test,
	/**
	 * Service work.
	 */
	service,
	/**
	 * Disconnect work.
	 */
	disconnect,
	/**
	 * (use 'connect' instead) Reconnect work.
	 */
	reconnect,
	/**
	 * Connect work.
	 */
	connect,
	/**
	 * Other kind of work.
	 */
	other,
	/**
	 * Work related to asset refurbishment.
	 */
	refurbishment
}