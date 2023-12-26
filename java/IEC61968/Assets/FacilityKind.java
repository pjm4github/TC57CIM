package IEC61968.Assets;


/**
 * Types of facilities at which an asset can be deployed.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public enum FacilityKind {
	substationHydroPlant,
	substationFossilPlant,
	substationNuclearPlant,
	substationTransmission,
	substationSubTransmission,
	substationDistribution,
	distributionPoleTop
}