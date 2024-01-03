package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.RealEnergy;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * Compressed air energy storage plant.
 * @created 02-Jan-2024 10:51:26 PM
 */
public class CAESPlant extends PowerSystemResource {

	/**
	 * The rated energy storage capacity.
	 */
	public RealEnergy energyStorageCapacity;
	/**
	 * The CAES plant's gross rated generating capacity.
	 */
	public ActivePower ratedCapacityP;
	/**
	 * A thermal generating unit may be a member of a compressed air energy storage
	 * plant.
	 */
	public ThermalGeneratingUnit ThermalGeneratingUnit;
	/**
	 * An air compressor may be a member of a compressed air energy storage plant.
	 */
	public AirCompressor AirCompressor;

	public CAESPlant(){

	}
}//end CAESPlant