package IEC61970.Base.ICCPConfiguration;


/**
 * Defines the expected level of security to be negotiated.
 * @author herb
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public enum SecurityRequirementKind {
	/**
	 * Indicates that the actor does not support any security options
	 */
	not supported,
	/**
	 * Indicates that the transport level security, per IEC 62351-6, is required.
	 */
	transportSecurityRequired,
	applicationSecurityRequired
}