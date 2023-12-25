package TC57CIM.IEC61970.Base.ICCPConfiguration;


/**
 * Specifies the expected security mechanism, per IEC 62351-6, to be utilized.
 * @author herb
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public enum IEC62351-6ApplicationSecurityKind {
	/**
	 * Indicates that the link does not require security.
	 */
	noSecurity,
	/**
	 * Indicates that authentication based upon ACSE is required.
	 */
	applicationLevel,
	/**
	 * Indicates that the Edition 3, end-to-end security is needed. (this would not be
	 * utilized for ICCP, but for IEC 61850).
	 */
	end-to-end
}