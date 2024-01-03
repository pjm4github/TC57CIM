package IEC61970.Base.Core;

import IEC61970.Base.Domain.Boolean;

/**
 * A collection of power system resources (within a given substation) including
 * conducting equipment, protection relays, measurements, and telemetry.  A bay
 * typically represents a physical grouping related to modularization of equipment.
 * 
 * @created 02-Jan-2024 10:17:31 PM
 */
public class Bay extends EquipmentContainer {

	/**
	 * Indicates the presence/absence of energy measurements.
	 */
	public Boolean bayEnergyMeasFlag;
	/**
	 * Indicates the presence/absence of active/reactive power measurements.
	 */
	public Boolean bayPowerMeasFlag;
	/**
	 * Breaker configuration. 
	 */
	public BreakerConfiguration breakerConfiguration;
	/**
	 * Bus bar configuration.
	 */
	public BusbarConfiguration busBarConfiguration;

	public Bay(){

	}
}//end Bay