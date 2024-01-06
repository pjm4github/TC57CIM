package IEC61970.Base.AuxiliaryEquipment;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.ActivePower;

/**
 * Instrument transformer used to measure electrical qualities of the circuit that
 * is being protected and/or monitored. Typically used as current transducer for
 * the purpose of metering or protection. A typical secondary current rating would
 * be 5A.
 * @created 02-Jan-2024 10:10:53 PM
 */
public class CurrentTransformer extends Sensor {

	/**
	 * CT accuracy classification.
	 */
	public String accuracyClass;
	/**
	 * Percent of rated current for which the CT remains accurate within specified
	 * limits.
	 */
	public PerCent accuracyLimit;
	/**
	 * Power burden of the CT core.
	 */
	public ActivePower coreBurden;
	/**
	 * CT classification; i.e. class 10P.
	 */
	public String ctClass;
	/**
	 * Intended usage of the CT; i.e. metering, protection.
	 */
	public String usage;

	public CurrentTransformer(){

	}
}//end CurrentTransformer