package IEC61970.InfIEC61970.InfSIPS;


/**
 * Categorisation of type of compare done on Equipment.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:36:27 PM
 */
public enum PinEquipmentKind {
	/**
	 * Check if equipment is in service, True if in service otherwise false.
	 */
	inService,
	/**
	 * Compare load flow result against rated current on the equipment (switch).
	 */
	ratedCurrent,
	/**
	 * Compare load flow result against the active voltage limit for the equipment.
	 */
	voltageLimit,
	/**
	 * Compare load flow result against the active current limit for the equipment.
	 */
	currentLimit,
	/**
	 * Compare load flow result against the active limit for active power for the
	 * given equipment.
	 */
	activePowerLimit,
	/**
	 * Compare load flow result against the active limit for apparent power for the
	 * given equipment.
	 */
	apparentPowerLimit,
	/**
	 * Check if all terminal on the equipment is connected.
	 */
	connected
}