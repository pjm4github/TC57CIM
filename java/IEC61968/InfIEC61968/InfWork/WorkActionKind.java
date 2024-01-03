package IEC61968.InfIEC61968.InfWork;


/**
 * Kinds of activities to be performed on a Compatible Unit.
 * @created 02-Jan-2024 9:58:07 PM
 */
public enum WorkActionKind {
	/**
	 * Install.
	 */
	install,
	/**
	 * Remove.
	 */
	remove,
	/**
	 * Leave it in place but not use it.
	 */
	abandon,
	/**
	 * Remove from one and install at another loctation.
	 */
	transfer
}