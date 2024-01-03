package IEC61970.Base.SCADA;


/**
 * Source gives information related to the origin of a value.
 * @created 02-Jan-2024 11:31:01 PM
 */
public enum Source {
	/**
	 * The value is provided by input from the process I/O or being calculated from
	 * some function.
	 */
	PROCESS,
	/**
	 * The value contains a default value.
	 */
	DEFAULTED,
	/**
	 * The value is provided by input of an operator or by an automatic source.
	 */
	SUBSTITUTED
}