package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;


/**
 * Governor droop signal feedback source.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public enum DroopSignalFeedbackKind {
	/**
	 * Electrical power feedback (connection indicated as 1 in the block diagrams of
	 * models, e.g. GovCT1, GovCT2).
	 */
	electricalPower,
	/**
	 * No droop signal feedback, is isochronous governor.
	 */
	none,
	/**
	 * Fuel valve stroke feedback (true stroke) (connection indicated as 2 in the
	 * block diagrams of model, e.g. GovCT1, GovCT2).
	 */
	fuelValveStroke,
	/**
	 * Governor output feedback (requested stroke) (connection indicated as 3 in the
	 * block diagrams of models, e.g. GovCT1, GovCT2).
	 */
	governorOutput
}