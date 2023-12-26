package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;

/**
 * Type of connection for the UEL input used in ExcIEEEST1A.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public enum ExcIEEEST1AUELselectorKind {
	/**
	 * Ignore UEL signal.
	 */
	ignoreUELsignal,
	/**
	 * UEL input HV gate with voltage regulator output.
	 */
	inputHVgateVoltageOutput,
	/**
	 * UEL input HV gate with error signal.
	 */
	inputHVgateErrorSignal,
	/**
	 * UEL input added to error signal.
	 */
	inputAddedToErrorSignal
}