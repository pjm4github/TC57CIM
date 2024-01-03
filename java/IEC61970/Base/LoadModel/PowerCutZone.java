package IEC61970.Base.LoadModel;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Wires.EnergyConsumer;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * An area or zone of the power system which is used for load shedding purposes.
 * @created 02-Jan-2024 11:13:41 PM
 */
public class PowerCutZone extends PowerSystemResource {

	/**
	 * First level (amount) of load to cut as a percentage of total zone load.
	 */
	public PerCent cutLevel1;
	/**
	 * Second level (amount) of load to cut as a percentage of total zone load.
	 */
	public PerCent cutLevel2;
	/**
	 * Energy consumer is assigned to the power cut zone.
	 */
	public EnergyConsumer EnergyConsumers;

	public PowerCutZone(){

	}
}//end PowerCutZone