package IEC61970.Base.AuxiliaryEquipment;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Float;

/**
 * Instrument transformer (also known as Voltage Transformer) used to measure
 * electrical qualities of the circuit that is being protected and/or monitored.
 * Typically used as voltage transducer for the purpose of metering, protection,
 * or sometimes auxiliary substation supply. A typical secondary voltage rating
 * would be 120V.
 * @created 02-Jan-2024 10:11:30 PM
 */
public class PotentialTransformer extends Sensor {

	/**
	 * PT accuracy classification.
	 */
	public String accuracyClass;
	/**
	 * Nominal ratio between the primary and secondary voltage.
	 */
	public Float nominalRatio;
	/**
	 * Potential transformer (PT) classification covering burden.
	 */
	public String ptClass;
	/**
	 * Potential transformer construction type.
	 */
	public PotentialTransformerKind type;

	public PotentialTransformer(){

	}
}//end PotentialTransformer