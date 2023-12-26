package IEC61968.Assets;


/**
 * Reason for breaker failure.
 * Note: This enumeration provides essential information to asset health analytics.
 * The existing list is a starting point and is anticipated to be fleshed out
 * further as requirements are better understood (PAB 2016/01/09).
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public enum BreakerFailureReasonKind {
	blastValveFailure,
	bushingFailure,
	closeCoilOpenShortedFailed,
	contaminatedAir,
	contaminatedArcChutes,
	contaminatedGas,
	contaminatedGasAir,
	controlCircuitFailure,
	degradedLubrication,
	externalOrInternalContamination,
	highPressureAirPlant,
	highResistanceLoadPath,
	highResistancePath,
	interrupterContactFailure,
	interrupterFailure,
	linkageFailure,
	lossOfOil,
	lossOfVacuum,
	lowGasPressure,
	mechanismFailure,
	mechanismOrLinkageFailure,
	oilRelatedFailure,
	poorOilQuality,
	rackingMechanismFailure,
	resistorFailure,
	resistorGradingCapacitorFailure,
	SF6BlastValveFailure,
	SF6PufferFailure,
	solidDielectricFailure,
	storedEnergyFailure,
	tripCoilOpenShortedFailed
}