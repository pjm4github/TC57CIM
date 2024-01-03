package IEC62325.MarketOperations.MktDomain;


/**
 * For example:
 * Bio Gas (Landfill, Sewage, Digester, etc.)
 * Biomass
 * Coal
 * DIST
 * Natural Gas
 * Geothermal
 * HRCV
 * None
 * Nuclear
 * Oil
 * Other
 * Solar
 * Waste to Energy
 * Water
 * Wind
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum FuelSource {
	/**
	 * Natural Gas
	 */
	NG,
	/**
	 * Non-Natural Gas
	 */
	NNG,
	/**
	 * Bio Gas (Landfill, Sewage, Digester, etc.)
	 */
	BGAS,
	/**
	 * Biomass
	 */
	BIOM,
	/**
	 * Coal
	 */
	COAL,
	DIST,
	GAS,
	/**
	 * GeoThermal
	 */
	GEOT,
	HRCV,
	NONE,
	/**
	 * Nuclear
	 */
	NUCL,
	OIL,
	/**
	 * Other
	 */
	OTHR,
	/**
	 * Solar
	 */
	SOLR,
	/**
	 * Waste to Energy
	 */
	WAST,
	/**
	 * Water
	 */
	WATR,
	/**
	 * Wind
	 */
	WIND
}