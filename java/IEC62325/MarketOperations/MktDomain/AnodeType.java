package IEC62325.MarketOperations.MktDomain;


/**
 * Aggregated Nodes Types for example:
 * <ul>
 * 	<li>SYS - System Zone/Region; </li>
 * </ul>
 * <ul>
 * 	<li>RUC - RUC Zone; </li>
 * </ul>
 * <ul>
 * 	<li>LFZ - Load Forecast Zone; </li>
 * </ul>
 * <ul>
 * 	<li>REG - Market Energy/Ancillary Service Region; </li>
 * </ul>
 * <ul>
 * 	<li>AGR - Aggregate Generation Resource; </li>
 * </ul>
 * <ul>
 * 	<li>POD - Point of Delivery; </li>
 * </ul>
 * <ul>
 * 	<li>ALR - Aggregate Load Resource; </li>
 * </ul>
 * <ul>
 * 	<li>LTAC - Load TransmissionAccessCharge (TAC) Group;</li>
 * </ul>
 * <ul>
 * 	<li>ACA - Adjacent Control Area</li>
 * </ul>
 * <ul>
 * 	<li>ASR - Aggregated System Resource</li>
 * </ul>
 * <ul>
 * 	<li>ECA - Embedded Control Area</li>
 * </ul>
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum AnodeType {
	/**
	 * System Zone/Region; 
	 */
	SYS,
	/**
	 * RUC Zone
	 */
	RUC,
	/**
	 * Load Forecast Zone
	 */
	LFZ,
	/**
	 * Market Energy/Ancillary Service Region; 
	 */
	REG,
	/**
	 * Aggregate Generation Resource; 
	 */
	AGR,
	/**
	 * Point of Delivery; 
	 */
	POD,
	/**
	 * Aggregate Load Resource; 
	 */
	ALR,
	/**
	 * Load TransmissionAccessCharge (TAC) Group;
	 */
	LTAC,
	/**
	 * Adjacent Control Area
	 */
	ACA,
	/**
	 * Aggregated System Resource
	 */
	ASR,
	/**
	 * Embedded Control Area
	 */
	ECA,
	/**
	 * Distributed Energy Resource.
	 */
	DER
}