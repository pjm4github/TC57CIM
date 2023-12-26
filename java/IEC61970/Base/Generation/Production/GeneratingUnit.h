///////////////////////////////////////////////////////////
//  GeneratingUnit.h
//  Implementation of the Class GeneratingUnit
//  Created on:      25-Dec-2023 8:31:58 PM
///////////////////////////////////////////////////////////

#if !defined(EA_8043C652_B0B8_4ca5_B75B_D93407EEEC08__INCLUDED_)
#define EA_8043C652_B0B8_4ca5_B75B_D93407EEEC08__INCLUDED_

#include "ActivePower.h"
#include "Seconds.py"
#include "ActivePowerChangeRate.h"
#include "PerCent.py"
#include "GeneratorControlMode.py"
#include "GeneratorControlSource.h"
#include "PU.h"
#include "Float.h"
#include "Classification.py"
#include "Money.py"
#include "java\IEC61970\IEC61970\Base\Wires\RotatingMachine.java"
#include "Equipment.py"
#include "GenUnitOpSchedule.h"
#include "GrossToNetActivePowerCurve.h"
#include "GenUnitOpCostCurve.py"

/**
 * A single or set of synchronous machines for converting mechanical power into
 * alternating-current power. For example, individual machines within a set may be
 * defined for scheduling purposes while a single control signal is derived for
 * the set. In this case there would be a GeneratingUnit for each member of the
 * set and an additional GeneratingUnit corresponding to the set.
 */
class GeneratingUnit : public Equipment
{

public:
	GeneratingUnit();
	/**
	 * The planned unused capacity (spinning reserve) which can be used to support
	 * emergency load.
	 */
	ActivePower allocSpinResP;
	/**
	 * The planned unused capacity which can be used to support automatic control
	 * overruns.
	 */
	ActivePower autoCntrlMarginP;
	/**
	 * For dispatchable units, this value represents the economic active power
	 * basepoint, for units that are not dispatchable, this value represents the fixed
	 * generation value. The value must be between the operating low and high limits.
	 */
	ActivePower baseP;
	/**
	 * Unit control error deadband. When a unit's desired active power change is less
	 * than this deadband, then no control pulses will be sent to the unit.
	 */
	ActivePower controlDeadband;
	/**
	 * Pulse high limit which is the largest control pulse that the unit can respond
	 * to.
	 */
	Seconds controlPulseHigh;
	/**
	 * Pulse low limit which is the smallest control pulse that the unit can respond
	 * to.
	 */
	Seconds controlPulseLow;
	/**
	 * Unit response rate which specifies the active power change for a control pulse
	 * of one second in the most responsive loading level of the unit.
	 */
	ActivePowerChangeRate controlResponseRate;
	/**
	 * The efficiency of the unit in converting mechanical energy, from the prime
	 * mover, into electrical energy.
	 */
	PerCent efficiency;
	/**
	 * The unit control mode.
	 */
	GeneratorControlMode genControlMode;
	/**
	 * The source of controls for a generating unit.
	 */
	GeneratorControlSource genControlSource;
	/**
	 * Governor motor position limit.
	 */
	PU governorMPL;
	/**
	 * Governor Speed Changer Droop.   This is the change in generator power output
	 * divided by the change in frequency normalized by the nominal power of the
	 * generator and the nominal frequency and expressed in percent and negated. A
	 * positive value of speed change droop provides additional generator output upon
	 * a drop in frequency.
	 */
	PerCent governorSCD;
	/**
	 * High limit for secondary (AGC) control.
	 */
	ActivePower highControlLimit;
	/**
	 * Default initial active power  which is used to store a powerflow result for the
	 * initial active power for this unit in this network configuration.
	 */
	ActivePower initialP;
	/**
	 * Generating unit long term economic participation factor.
	 */
	Float longPF;
	/**
	 * Low limit for secondary (AGC) control.
	 */
	ActivePower lowControlLimit;
	/**
	 * The normal maximum rate the generating unit active power output can be lowered
	 * by control actions.
	 */
	ActivePowerChangeRate lowerRampRate;
	/**
	 * Maximum high economic active power limit, that should not exceed the maximum
	 * operating active power limit.
	 */
	ActivePower maxEconomicP;
	/**
	 * Maximum allowable spinning reserve. Spinning reserve will never be considered
	 * greater than this value regardless of the current operating point.
	 */
	ActivePower maximumAllowableSpinningReserve;
	/**
	 * This is the maximum operating active power limit the dispatcher can enter for
	 * this unit.
	 */
	ActivePower maxOperatingP;
	/**
	 * Low economic active power limit that must be greater than or equal to the
	 * minimum operating active power limit.
	 */
	ActivePower minEconomicP;
	/**
	 * Minimum time interval between unit shutdown and startup.
	 */
	Seconds minimumOffTime;
	/**
	 * This is the minimum operating active power limit the dispatcher can enter for
	 * this unit.
	 */
	ActivePower minOperatingP;
	/**
	 * Detail level of the generator model data.
	 */
	Classification modelDetail;
	/**
	 * The nominal power of the generating unit.  Used to give precise meaning to
	 * percentage based attributes such as the governor speed change droop
	 * (governorSCD attribute).
	 * The attribute shall be a positive value equal or less than RotatingMachine.
	 * ratedS.
	 */
	ActivePower nominalP;
	/**
	 * Generating unit economic participation factor.
	 */
	Float normalPF;
	/**
	 * Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental
	 * Transmission Loss expressed as a plus or minus value. The typical range of
	 * penalty factors is (0.9 to 1.1).
	 */
	Float penaltyFactor;
	/**
	 * The normal maximum rate the generating unit active power output can be raised
	 * by control actions.
	 */
	ActivePowerChangeRate raiseRampRate;
	/**
	 * The unit's gross rated maximum capacity (book value).
	 */
	ActivePower ratedGrossMaxP;
	/**
	 * The gross rated minimum generation level which the unit can safely operate at
	 * while delivering power to the transmission grid.
	 */
	ActivePower ratedGrossMinP;
	/**
	 * The net rated maximum capacity determined by subtracting the auxiliary power
	 * used to operate the internal plant machinery from the rated gross maximum
	 * capacity.
	 */
	ActivePower ratedNetMaxP;
	/**
	 * Generating unit short term economic participation factor.
	 */
	Float shortPF;
	/**
	 * The initial startup cost incurred for each start of the GeneratingUnit.
	 */
	Money startupCost;
	/**
	 * Time it takes to get the unit on-line, from the time that the prime mover
	 * mechanical power is applied.
	 */
	Seconds startupTime;
	/**
	 * Generating unit economic participation factor.
	 */
	Float tieLinePF;
	/**
	 * The efficiency of the unit in converting the fuel into electrical energy.
	 */
	PerCent totalEfficiency;
	/**
	 * The variable cost component of production per unit of ActivePower.
	 */
	Money variableCost;
	/**
	 * A synchronous machine may operate as a generator and as such becomes a member
	 * of a generating unit.
	 */
	RotatingMachine *RotatingMachine;
	/**
	 * A generating unit may have an operating schedule, indicating the planned
	 * operation of the unit.
	 */
	GenUnitOpSchedule *GenUnitOpSchedule;
	/**
	 * A generating unit may have a gross active power to net active power curve,
	 * describing the losses and auxiliary power requirements of the unit.
	 */
	GrossToNetActivePowerCurve *GrossToNetActivePowerCurves;
	/**
	 * A generating unit may have one or more cost curves, depending upon fuel mixture
	 * and fuel cost.
	 */
	GenUnitOpCostCurve *GenUnitOpCostCurves;

};
#endif // !defined(EA_8043C652_B0B8_4ca5_B75B_D93407EEEC08__INCLUDED_)
