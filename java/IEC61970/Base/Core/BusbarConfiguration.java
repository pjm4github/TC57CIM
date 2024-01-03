package IEC61970.Base.Core;


/**
 * Busbar layout for bay.
 * @created 02-Jan-2024 10:39:02 PM
 */
public enum BusbarConfiguration {
	/**
	 * Single bus.
	 */
	singleBus,
	/**
	 * Double bus.
	 */
	doubleBus,
	/**
	 * Main bus with transfer bus.
	 */
	mainWithTransfer,
	/**
	 * Ring bus.
	 */
	ringBus
}