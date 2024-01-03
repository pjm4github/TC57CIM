package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.CostRate;
import IEC61970.Base.Domain.CostPerEnergyUnit;
import IEC61970.Base.Domain.Hours;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Unit start up characteristics depending on how long the unit has been off line.
 * @created 02-Jan-2024 10:58:43 PM
 */
public class StartupModel extends IdentifiedObject {

	/**
	 * Fixed maintenance cost.
	 */
	public CostRate fixedMaintCost;
	/**
	 * The amount of heat input per time uint required for hot standby operation.
	 */
	public HeatRate hotStandbyHeat;
	/**
	 * Incremental maintenance cost.
	 */
	public CostPerEnergyUnit incrementalMaintCost;
	/**
	 * The minimum number of hours the unit must be down before restart.
	 */
	public Hours minimumDownTime;
	/**
	 * The minimum number of hours the unit must be operating before being allowed to
	 * shut down.
	 */
	public Hours minimumRunTime;
	/**
	 * The opportunity cost associated with the return in monetary unit. This
	 * represents the restart's "share" of the unit depreciation and risk of an event
	 * which would damage the unit.
	 */
	public Money riskFactorCost;
	/**
	 * Total miscellaneous start up costs.
	 */
	public Money startupCost;
	/**
	 * The date and time of the most recent generating unit startup.
	 */
	public DateTime startupDate;
	/**
	 * Startup priority within control area where lower numbers indicate higher
	 * priorities.  More than one unit in an area may be assigned the same priority.
	 */
	public Integer startupPriority;
	/**
	 * The unit's auxiliary active power consumption to maintain standby mode.
	 */
	public ActivePower stbyAuxP;
	/**
	 * The unit's startup model may have a startup ramp curve.
	 */
	public StartRampCurve StartRampCurve;
	/**
	 * The unit's startup model may have a startup ignition fuel curve.
	 */
	public StartIgnFuelCurve StartIgnFuelCurve;
	/**
	 * The unit's startup model may have a startup main fuel curve.
	 */
	public StartMainFuelCurve StartMainFuelCurve;

	public StartupModel(){

	}
}//end StartupModel