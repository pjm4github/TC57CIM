#######################################################
# 
# GeneratingUnit.py
# Python implementation of the Class GeneratingUnit
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 7:48:10 PM
# 
#######################################################
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Seconds import Seconds
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePowerChangeRate import ActivePowerChangeRate
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PerCent import PerCent
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Generation.Production.GeneratorControlMode import GeneratorControlMode
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Generation.Production.GeneratorControlSource import GeneratorControlSource
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PU import PU
# from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Float import Float
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Generation.Production.Classification import Classification
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Money import Money
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RotatingMachine import RotatingMachine
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Equipment import Equipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Generation.Production.GenUnitOpSchedule import GenUnitOpSchedule
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Generation.Production.GrossToNetActivePowerCurve import GrossToNetActivePowerCurve
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Generation.Production.GenUnitOpCostCurve import GenUnitOpCostCurve

class GeneratingUnit(Equipment):
    """A single or set of synchronous machines for converting mechanical power into
    alternating-current power. For example, individual machines within a set may be
    defined for scheduling purposes while a single control signal is derived for
    the set. In this case there would be a GeneratingUnit for each member of the
    set and an additional GeneratingUnit corresponding to the set.
    """

    def __init__(self):
        super().__init__()

        self.alloc_spin_res_p = ActivePower()  # The planned unused capacity (spinning reserve) which can be used to support emergency load.
        self.auto_cntrl_margin_p = ActivePower()  # The planned unused capacity which can be used to support automatic control overruns.
        self.base_p = ActivePower()  # For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits.
        self.control_deadband = ActivePower()  # Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit.
        self.control_pulse_high = Seconds()  # Pulse high limit which is the largest control pulse that the unit can respond to.
        self.control_pulse_low = Seconds()  # Pulse low limit which is the smallest control pulse that the unit can respond to.
        self.control_response_rate = ActivePowerChangeRate()  # Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit.
        self.efficiency = PerCent()  # The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy.
        self.gen_control_mode = GeneratorControlMode.PULSE  # The unit control mode.
        self.gen_control_source = GeneratorControlSource.UNAVAILABLE  # The source of controls for a generating unit.
        self.gen_unit_op_cost_curves = GenUnitOpCostCurve() # A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        self.gen_unit_op_schedule = GenUnitOpSchedule() # A generating unit may have an operating schedule, indicating the planned operation of the unit.
        self.governor_mpl = PU()  # Governor motor position limit.
        self.governor_scd = PerCent()  # Governor Speed Changer Droop. This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.
        self.gross_to_net_active_power_curves = GrossToNetActivePowerCurve() # A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit.
        self.high_control_limit = ActivePower()  # High limit for secondary (AGC) control.
        self.initial_p = ActivePower()  # Default initial active power which is used to store a powerflow result for the initial active power for this unit in this network configuration.
        self.long_pf = 0.0  # Generating unit long term economic participation factor.
        self.low_control_limit = ActivePower()  # Low limit for secondary (AGC) control.
        self.lower_ramp_rate = ActivePowerChangeRate()  # The normal maximum rate the generating unit active power output can be lowered by control actions.
        self.max_economic_p = ActivePower()  # Maximum high economic active power limit, that should not exceed the maximum operating active power limit.
        self.max_operating_p = ActivePower()  # This is the maximum operating active power limit the dispatcher can enter for this unit.
        self.maximum_allowable_spinning_reserve = ActivePower()  # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
        self.min_economic_p = ActivePower()  # Low economic active power limit that must be greater than or equal to the minimum operating active power limit.
        self.min_operating_p = ActivePower()  # This is the minimum operating active power limit the dispatcher can enter for this unit.
        self.minimum_off_time = Seconds()  # Minimum time interval between unit shutdown and startup.
        self.model_detail = Classification()  # Detail level of the generator model data.
        self.nominal_p = ActivePower()  # The nominal power of the generating unit. Used to give precise meaning to percentage based attributes such as the governor speed change droop (governor_scd attribute).
        self.normal_pf = 1.0  # Generating unit economic participation factor.
        self.penalty_factor = 0.0  # Defined as: 1 / (1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1).
        self.raise_ramp_rate = ActivePowerChangeRate()  # The normal maximum rate the generating unit active power output can be power output can be raised by control actions.
        self.rated_gross_max_p = ActivePower() # The unit's gross rated maximum capacity (book value).
        self.rated_gross_min_p = ActivePower() # The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid.
        self.rated_net_max_p = ActivePower() # The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity.
        self.rotating_machine = RotatingMachine() # A synchronous machine may operate as a generator and as such becomes a member of a generating unit.
        self.short_pf = 0.0 # Generating unit short term economic participation factor.
        self.startup_cost = Money() # The initial startup cost incurred for each start of the GeneratingUnit.
        self.startup_time = Seconds() # Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied.
        self.tie_line_pf = 0.0 # Generating unit economic participation factor.
        self.total_efficiency = PerCent() # The efficiency of the unit in converting the fuel into electrical energy.
        self.variable_cost = Money() # The variable cost component of production per unit of ActivePower.