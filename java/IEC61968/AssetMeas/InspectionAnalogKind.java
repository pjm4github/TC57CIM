package IEC61968.AssetMeas;


/**
 * Analogs typically recorded during a field inspection.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public enum InspectionAnalogKind {
	/**
	 * Can apply to whole breaker or any individual pole.
	 */
	SF6PressureReading,
	AirPressureReading,
	airPressureHPSystemReading,
	compressorHourMeterReading,
	/**
	 * Can apply to whole breaker or any individual pole.
	 */
	airPressureLPSystemReading
}