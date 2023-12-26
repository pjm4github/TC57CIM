package IEC61970.Dynamics.StandardInterconnections;


/**
 * Type of input signal coming from remote bus.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public enum RemoteSignalKind {
	/**
	 * Input is voltage frequency from remote terminal bus.
	 */
	remoteBusVoltageFrequency,
	/**
	 * Input is voltage frequency deviation from remote terminal bus.
	 */
	remoteBusVoltageFrequencyDeviation,
	/**
	 * Input is frequency from remote terminal bus.
	 */
	remoteBusFrequency,
	/**
	 * Input is frequency deviation from remote terminal bus.
	 */
	remoteBusFrequencyDeviation,
	/**
	 * Input is voltage amplitude from remote terminal bus.
	 */
	remoteBusVoltageAmplitude,
	/**
	 * Input is voltage from remote terminal bus.
	 */
	remoteBusVoltage,
	/**
	 * Input is branch current amplitude from remote terminal bus.
	 */
	remoteBranchCurrentAmplitude,
	/**
	 * Input is branch current amplitude derivative from remote terminal bus.
	 */
	remoteBusVoltageAmplitudeDerivative,
	/**
	 * Input is PU voltage derivative from remote terminal bus.
	 */
	remotePuBusVoltageDerivative
}