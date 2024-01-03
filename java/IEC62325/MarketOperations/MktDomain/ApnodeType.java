package IEC62325.MarketOperations.MktDomain;


/**
 * Aggregate Node Types for example:
 * AG -  Aggregated Generation
 * CPZ -  Custom Price Zone
 * DPZ -  Default Price Zone
 * LAP - Load Aggregation Point
 * TH -  Trading  Hub
 * SYS - System Zone
 * CA - Control Area
 * 
 * GA - generic aggregation
 * EHV - 500 kV
 * GH - generic hub
 * ZN - zone
 * INT - Interface
 * BUS - Bus
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum ApnodeType {
	/**
	 * Aggregated Generation
	 */
	AG,
	/**
	 * Custom Price Zone
	 */
	CPZ,
	/**
	 * Default Price Zone
	 */
	DPZ,
	/**
	 * Trading  Hub
	 */
	TH,
	/**
	 * System Zone
	 */
	SYS,
	/**
	 * Control Area
	 */
	CA,
	/**
	 * Designated Congestion Area
	 */
	DCA,
	/**
	 * generic aggregation
	 */
	GA,
	/**
	 * generic hub
	 */
	GH,
	/**
	 * 500 kV - Extra High Voltage aggregate price nodes
	 */
	EHV,
	/**
	 * Zone
	 */
	ZN,
	/**
	 * Interface
	 */
	INT,
	/**
	 * Bus
	 */
	BUS
}