package IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics;


/**
 * Type of synchronous machine model used in Dynamic simulation applications.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public enum SynchronousMachineModelKind {
	/**
	 * Subtransient synchronous machine model.
	 */
	subtransient,
	/**
	 * WECC Type F variant of subtransient synchronous machine model.
	 */
	subtransientTypeF,
	/**
	 * WECC Type J variant of subtransient synchronous machine model.
	 */
	subtransientTypeJ,
	/**
	 * Simplified version of subtransient synchronous machine model where magnetic
	 * coupling between the direct and quadrature axes is ignored.
	 */
	subtransientSimplified,
	/**
	 * Simplified version of a subtransient synchronous machine model with no damper
	 * circuit on d-axis. 
	 */
	subtransientSimplifiedDirectAxis
}