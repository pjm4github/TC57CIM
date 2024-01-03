package IEC61970.Base.Generation.GenerationTrainingSimulation;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Wires.SynchronousMachine;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * The machine used to develop mechanical energy used to drive a generator.
 * @created 02-Jan-2024 11:06:18 PM
 */
public class PrimeMover extends PowerSystemResource {

	/**
	 * Rating of prime mover.
	 */
	public Float primeMoverRating;
	/**
	 * Synchronous machines this Prime mover drives.
	 */
	public SynchronousMachine SynchronousMachines;

	public PrimeMover(){

	}
}//end PrimeMover