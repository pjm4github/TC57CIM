package IEC61970.Base.ICCPConfiguration;


/**
 * Provides access privilege information regarding an ICCP point.
 * @author herb
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public enum ICCPAccessPrivilegeKind {
	/**
	 * Indicates that the remote is not allowed to change the value of the ICCPPoint.
	 */
	readOnly,
	/**
	 * Indicates that the remote can not only get the value, but may also change the
	 * value of the ICCP Point.
	 */
	readWrite
}