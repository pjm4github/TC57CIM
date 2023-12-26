package IEC61968.Metering;


/**
 * Kind of read / measured value.
 * @author Marty
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public enum MeasurementKind {
	/**
	 * Not Applicable
	 */
	none,
	apparentPowerFactor,
	/**
	 * funds
	 */
	currency,
	current,
	currentAngle,
	currentImbalance,
	date,
	demand,
	distance,
	distortionVoltAmp,
	energization,
	energy,
	energizationLoadSide,
	fan,
	frequency,
	/**
	 * Dup with "currency"
	 */
	fund,
	ieee1366ASAI,
	ieee1366ASIDI,
	ieee1366ASIFI,
	ieee1366CAIDI,
	ieee1366CAIFI,
	ieee1366CEMIn,
	ieee1366CEMSMIn,
	ieee1366CTAIDI,
	ieee1366MAIFI,
	ieee1366MAIFIe,
	ieee1366SAIDI,
	ieee1366SAIFI,
	lineLoss,
	loss,
	negativeSequence,
	phasorPowerFactor,
	phasorReactivePower,
	positiveSequence,
	power,
	powerFactor,
	quantityPower,
	/**
	 * or Voltage Dip
	 */
	sag,
	swell,
	switchPosition,
	tapPosition,
	tariffRate,
	temperature,
	totalHarmonicDistortion,
	transformerLoss,
	unipedeVoltageDip10to15,
	unipedeVoltageDip15to30,
	unipedeVoltageDip30to60,
	unipedeVoltageDip60to90,
	unipedeVoltageDip90to100,
	voltage,
	voltageAngle,
	voltageExcursion,
	voltageImbalance,
	/**
	 * Clarified  from Ed. 1. to indicate fluid volume
	 */
	volume,
	zeroFlowDuration,
	zeroSequence,
	distortionPowerFactor,
	/**
	 * Usually expressed as a "count"
	 */
	frequencyExcursion,
	applicationContext,
	apTitle,
	assetNumber,
	bandwidth,
	batteryVoltage,
	broadcastAddress,
	deviceAddressType1,
	deviceAddressType2,
	deviceAddressType3,
	deviceAddressType4,
	deviceClass,
	electronicSerialNumber,
	endDeviceID,
	groupAddressType1,
	groupAddressType2,
	groupAddressType3,
	groupAddressType4,
	ipAddress,
	macAddress,
	mfgAssignedConfigurationID,
	mfgAssignedPhysicalSerialNumber,
	mfgAssignedProductNumber,
	mfgAssignedUniqueCommunicationAddress,
	multiCastAddress,
	oneWayAddress,
	signalStrength,
	twoWayAddress,
	/**
	 * Moved here from Attribute #9 UOM
	 */
	signaltoNoiseRatio,
	alarm,
	batteryCarryover,
	dataOverflowAlarm,
	demandLimit,
	/**
	 * Usually expressed as a count as part of a billing cycle
	 */
	demandReset,
	diagnostic,
	emergencyLimit,
	encoderTamper,
	ieee1366MomentaryInterruption,
	ieee1366MomentaryInterruptionEvent,
	ieee1366SustainedInterruption,
	interruptionBehaviour,
	inversionTamper,
	loadInterrupt,
	loadShed,
	maintenance,
	physicalTamper,
	powerLossTamper,
	powerOutage,
	powerQuality,
	powerRestoration,
	programmed,
	pushbutton,
	relayActivation,
	/**
	 * Usually expressed as a count
	 */
	relayCycle,
	removalTamper,
	reprogrammingTamper,
	reverseRotationTamper,
	switchArmed,
	switchDisabled,
	tamper,
	watchdogTimeout,
	/**
	 * Customer's bill for the previous billing period (Currency)
	 */
	billLastPeriod,
	/**
	 * Customer's bill, as known thus far within the present billing period (Currency)
	 */
	billToDate,
	/**
	 * Customer's bill for the (Currency)
	 */
	billCarryover,
	/**
	 * Monthly fee for connection to commodity.
	 */
	connectionFee,
	/**
	 * Sound
	 */
	audibleVolume,
	volumetricFlow
}