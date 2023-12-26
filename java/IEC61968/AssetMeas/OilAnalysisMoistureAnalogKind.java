package IEC61968.AssetMeas;


/**
 * Analogs representing oil moisture analysis result.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public enum OilAnalysisMoistureAnalogKind {
	/**
	 * Moisture measured via coulometric Karl Fischer titration (in ppm, specifically
	 * milligram/kilogram).
	 */
	waterContent,
	/**
	 * Water content by infrared sensor (in ppm, specifically milligram/kilogram).
	 */
	waterContentMonitoredViaInfrared,
	/**
	 * Water content by capacitance sensor (in ppm, specifically milligram/kilogram).
	 */
	waterContentMonitoredViaCapacitance,
	/**
	 * Water content by aluminum oxide sensor (in ppm, specifically
	 * milligram/kilogram).
	 */
	waterContentMonitoredViaAluminumOxide,
	/**
	 * Water content by other sensor (in ppm, specifically milligram/kilogram).
	 */
	waterContentMonitoredViaOther,
	/**
	 * Relative saturation of water in fluid (in percent).
	 */
	relativeSaturation,
	/**
	 * Calculated relative saturation of water in fluid (in percent).
	 */
	relativeSaturationCalculated,
	/**
	 * Dew point (in øC). Is usually a negative value.
	 */
	dewPoint
}