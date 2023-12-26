package IEC61970.Dynamics.StandardModels.LoadDynamics;

import IEC61970.Base.Domain.PU;

/**
 * Type of generic non-linear load model.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public enum GenericNonLinearLoadModelKind {
	/**
	 * Exponential recovery model.
	 */
	exponentialRecovery,
	/**
	 * Load adaptive model.
	 */
	loadAdaptive
}