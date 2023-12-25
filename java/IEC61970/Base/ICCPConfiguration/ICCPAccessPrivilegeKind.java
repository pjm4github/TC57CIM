package TC57CIM.IEC61970.Base.ICCPConfiguration;


/**
 * Provides access privilege information regarding an ICCP point.
 * @author herb
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
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