package IEC61970.Base.Generation.Production;


/**
 * Specifies the capability of the hydro generating unit to convert energy as a
 * generator or pump.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public enum HydroEnergyConversionKind {
	/**
	 * Able to generate power, but not able to pump water for energy storage.
	 */
	generator,
	/**
	 * Able to both generate power and pump water for energy storage.
	 */
	pumpAndGenerator
}