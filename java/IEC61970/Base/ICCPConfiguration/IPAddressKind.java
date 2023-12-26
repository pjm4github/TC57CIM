package IEC61970.Base.ICCPConfiguration;


/**
 * Indicates if the addressing of the IPAccessPoint, gateway, and subnet are per
 * IPv4 or IPv6
 * @author herb
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public enum IPAddressKind {
	/**
	 * Indicates that IPv4 dotted decimal notation is in use.
	 */
	IPv4,
	/**
	 * Indicates that an IPv6 dotted decimal is in use.
	 */
	IPv6
}