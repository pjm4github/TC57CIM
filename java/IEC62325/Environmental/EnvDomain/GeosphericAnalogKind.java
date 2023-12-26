package IEC62325.Environmental.EnvDomain;


/**
 * Kinds of analogs (floats) measuring a geospheric condition.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public enum GeosphericAnalogKind {
	/**
	 * Flash rate in strikes/hour/km<sup>2</sup>.
	 */
	lightningDensity,
	seismicEastWest,
	seismicNorthSouth,
	seismicVertical,
	snowPackDepth,
	temperature
}