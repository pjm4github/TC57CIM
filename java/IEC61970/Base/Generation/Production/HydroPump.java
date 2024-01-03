package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.VolumeFlowRate;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Core.Equipment;

/**
 * A synchronous motor-driven pump, typically associated with a pumped storage
 * plant.
 * @created 02-Jan-2024 10:55:42 PM
 */
public class HydroPump extends Equipment {

	/**
	 * The pumping discharge under maximum head conditions, usually at full gate.
	 */
	public VolumeFlowRate pumpDischAtMaxHead;
	/**
	 * The pumping discharge under minimum head conditions, usually at full gate.
	 */
	public VolumeFlowRate pumpDischAtMinHead;
	/**
	 * The pumping power under maximum head conditions, usually at full gate.
	 */
	public ActivePower pumpPowerAtMaxHead;
	/**
	 * The pumping power under minimum head conditions, usually at full gate.
	 */
	public ActivePower pumpPowerAtMinHead;
	/**
	 * The hydro pump has a pumping schedule over time, indicating when pumping is to
	 * occur.
	 */
	public HydroPumpOpSchedule HydroPumpOpSchedule;

	public HydroPump(){

	}
}//end HydroPump