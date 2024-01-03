package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.ActivePowerChangeRate;
import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Wires.RotatingMachine;
import IEC61970.Base.Core.Equipment;

/**
 * A single or set of synchronous machines for converting mechanical power into
 * alternating-current power. For example, individual machines within a set may be
 * defined for scheduling purposes while a single control signal is derived for
 * the set. In this case there would be a GeneratingUnit for each member of the
 * set and an additional GeneratingUnit corresponding to the set.
 * @created 02-Jan-2024 10:54:02 PM
 */
public class GeneratingUnit extends Equipment {

	/**
	 * The planned unused capacity (spinning reserve) which can be used to support
	 * emergency load.
	 */
	public ActivePower allocSpinResP;
	/**
	 * The planned unused capacity which can be used to support automatic control
	 * overruns.
	 */
	public ActivePower autoCntrlMarginP;
	/**
	 * For dispatchable units, this value represents the economic active power
	 * basepoint, for units that are not dispatchable, this value represents the fixed
	 * generation value. The value must be between the operating low and high limits.
	 */
	public ActivePower baseP;
	/**
	 * Unit control error deadband. When a unit's desired active power change is less
	 * than this deadband, then no control pulses will be sent to the unit.
	 */
	public ActivePower controlDeadband;
	/**
	 * Pulse high limit which is the largest control pulse that the unit can respond
	 * to.
	 */
	public Seconds controlPulseHigh;
	/**
	 * Pulse low limit which is the smallest control pulse that the unit can respond
	 * to.
	 */
	public Seconds controlPulseLow;
	/**
	 * Unit response rate which specifies the active power change for a control pulse
	 * of one second in the most responsive loading level of the unit.
	 */
	public ActivePowerChangeRate controlResponseRate;
	/**
	 * The efficiency of the unit in converting mechanical energy, from the prime
	 * mover, into electrical energy.
	 */
	public PerCent efficiency;
	/**
	 * The unit control mode.
	 */
	public GeneratorControlMode genControlMode;
	/**
	 * The source of controls for a generating unit.
	 */
	public GeneratorControlSource genControlSource;
	/**
	 * Governor motor position limit.
	 */
	public PU governorMPL;
	/**
	 * Governor Speed Changer Droop.   This is the change in generator power output
	 * divided by the change in frequency normalized by the nominal power of the
	 * generator and the nominal frequency and expressed in percent and negated. A
	 * positive value of speed change droop provides additional generator output upon
	 * a drop in frequency.
	 */
	public PerCent governorSCD;
	/**
	 * High limit for secondary (AGC) control.
	 */
	public ActivePower highControlLimit;
	/**
	 * Default initial active power  which is used to store a powerflow result for the
	 * initial active power for this unit in this network configuration.
	 */
	public ActivePower initialP;
	/**
	 * Generating unit long term economic participation factor.
	 */
	public Float longPF;
	/**
	 * Low limit for secondary (AGC) control.
	 */
	public ActivePower lowControlLimit;
	/**
	 * The normal maximum rate the generating unit active power output can be lowered
	 * by control actions.
	 */
	public ActivePowerChangeRate lowerRampRate;
	/**
	 * Maximum high economic active power limit, that should not exceed the maximum
	 * operating active power limit.
	 */
	public ActivePower maxEconomicP;
	/**
	 * Maximum allowable spinning reserve. Spinning reserve will never be considered
	 * greater than this value regardless of the current operating point.
	 */
	public ActivePower maximumAllowableSpinningReserve;
	/**
	 * This is the maximum operating active power limit the dispatcher can enter for
	 * this unit.
	 */
	public ActivePower maxOperatingP;
	/**
	 * Low economic active power limit that must be greater than or equal to the
	 * minimum operating active power limit.
	 */
	public ActivePower minEconomicP;
	/**
	 * Minimum time interval between unit shutdown and startup.
	 */
	public Seconds minimumOffTime;
	/**
	 * This is the minimum operating active power limit the dispatcher can enter for
	 * this unit.
	 */
	public ActivePower minOperatingP;
	/**
	 * Detail level of the generator model data.
	 */
	public Classification modelDetail;
	/**
	 * The nominal power of the generating unit.  Used to give precise meaning to
	 * percentage based attributes such as the governor speed change droop
	 * (governorSCD attribute).
	 * The attribute shall be a positive value equal or less than RotatingMachine.
	 * ratedS.
	 */
	public ActivePower nominalP;
	/**
	 * Generating unit economic participation factor.
	 */
	public Float normalPF;
	/**
	 * Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental
	 * Transmission Loss expressed as a plus or minus value. The typical range of
	 * penalty factors is (0.9 to 1.1).
	 */
	public Float penaltyFactor;
	/**
	 * The normal maximum rate the generating unit active power output can be raised
	 * by control actions.
	 */
	public ActivePowerChangeRate raiseRampRate;
	/**
	 * The unit's gross rated maximum capacity (book value).
	 */
	public ActivePower ratedGrossMaxP;
	/**
	 * The gross rated minimum generation level which the unit can safely operate at
	 * while delivering power to the transmission grid.
	 */
	public ActivePower ratedGrossMinP;
	/**
	 * The net rated maximum capacity determined by subtracting the auxiliary power
	 * used to operate the internal plant machinery from the rated gross maximum
	 * capacity.
	 */
	public ActivePower ratedNetMaxP;
	/**
	 * Generating unit short term economic participation factor.
	 */
	public Float shortPF;
	/**
	 * The initial startup cost incurred for each start of the GeneratingUnit.
	 */
	public Money startupCost;
	/**
	 * Time it takes to get the unit on-line, from the time that the prime mover
	 * mechanical power is applied.
	 */
	public Seconds startupTime;
	/**
	 * Generating unit economic participation factor.
	 */
	public Float tieLinePF;
	/**
	 * The efficiency of the unit in converting the fuel into electrical energy.
	 */
	public PerCent totalEfficiency;
	/**
	 * The variable cost component of production per unit of ActivePower.
	 */
	public Money variableCost;
	/**
	 * A synchronous machine may operate as a generator and as such becomes a member
	 * of a generating unit.
	 */
	public RotatingMachine RotatingMachine;
	/**
	 * A generating unit may have an operating schedule, indicating the planned
	 * operation of the unit.
	 */
	public GenUnitOpSchedule GenUnitOpSchedule;
	/**
	 * A generating unit may have a gross active power to net active power curve,
	 * describing the losses and auxiliary power requirements of the unit.
	 */
	public GrossToNetActivePowerCurve GrossToNetActivePowerCurves;
	/**
	 * A generating unit may have one or more cost curves, depending upon fuel mixture
	 * and fuel cost.
	 */
	public GenUnitOpCostCurve GenUnitOpCostCurves;

	public GeneratingUnit(){

	}
}//end GeneratingUnit