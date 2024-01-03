package IEC61970.Base.Core;

import IEC61970.Base.Domain.Voltage;

/**
 * A collection of equipment at one common system voltage forming a switchgear.
 * The equipment typically consist of breakers, busbars, instrumentation, control,
 * regulation and protection devices as well as assemblies of all these.
 * @created 02-Jan-2024 10:38:24 PM
 */
public class VoltageLevel extends EquipmentContainer {

	/**
	 * The bus bar's high voltage limit
	 */
	public Voltage highVoltageLimit;
	/**
	 * The bus bar's low voltage limit
	 */
	public Voltage lowVoltageLimit;
	/**
	 * The bays within this voltage level.
	 */
	public Bay Bays;
	/**
	 * The base voltage used for all equipment within the voltage level.
	 */
	public BaseVoltage BaseVoltage;

	public VoltageLevel(){

	}
}//end VoltageLevel