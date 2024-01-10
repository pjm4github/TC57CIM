# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.ActivePowerChangeRate import ActivePowerChangeRate
from IEC61970.Base.Domain.CostPerEnergyUnit import CostPerEnergyUnit
from IEC61970.Base.Domain.CostRate import CostRate
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Generation.Production.CostPerHeatUnit import CostPerHeatUnit
from IEC62325.MarketOperations.MktDomain.CostBasis import CostBasis
from IEC62325.MarketOperations.MktDomain.FlagTypeRMR import FlagTypeRMR
from IEC62325.MarketOperations.MktDomain.FuelSource import FuelSource
from IEC62325.MarketOperations.MktDomain.RampCurveType import RampCurveType
from IEC62325.MarketOperations.MktDomain.UnitRegulationKind import UnitRegulationKind
from IEC62325.MarketOperations.MktDomain.UnitType import UnitType
# from IEC62325.MarketOperations.ReferenceData.RMRHeatRateCurve import RMRHeatRateCurve
# from IEC62325.MarketOperations.ReferenceData.RMRStartUpFuelCurve import RMRStartUpFuelCurve
# from IEC62325.MarketOperations.ReferenceData.RegulatingLimit import RegulatingLimit
# from IEC62325.MarketOperations.ReferenceData.RMRStartUpCostCurve import RMRStartUpCostCurve
# from IEC62325.MarketOperations.ReferenceData.RMRStartUpEnergyCurve import RMRStartUpEnergyCurve
# from IEC62325.MarketOperations.ReferenceData.RMRStartUpTimeCurve import RMRStartUpTimeCurve
from IEC62325.MarketOperations.ReferenceData.ResourceCertification import YesNo
# from IEC62325.MarketOperations.ReferenceData.StartUpFuelCurve import StartUpFuelCurve
# from IEC62325.MarketOperations.ReferenceData.StartUpEnergyCurve import StartUpEnergyCurve
# from IEC62325.MarketOperations.ReferenceData.MktHeatRateCurve import MktHeatRateCurve
from IEC62325.MarketOperations.ParticipantInterfaces.GeneratingBid import GeneratingBid
from IEC62325.MarketOperations.ParticipantInterfaces.Trade import Trade
from IEC62325.MarketOperations.ParticipantInterfaces.StartUpTimeCurve import StartUpTimeCurve
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource


# from IEC61970.Base.Domain import PerCent, Float, String, DateTime
# from IEC62325.MarketOperations.MktDomain import YesNo, FuelSource, RampCurveType, UnitRegulationKind, FlagTypeRMR,
# UnitType
# from IEC61970.Base.Domain import ActivePowerChangeRate, ActivePower, CostRate, Integer, CostBasis, CostPerHeatUnit,
# CostPerEnergyUnit
# from IEC61970.Base.Domain import PerCent, Float, String, DateTime
# from IEC62325.MarketOperations.MktDomain import YesNo, ActivePowerChangeRate, FuelSource, RampCurveType,
# UnitRegulationKind, FlagTypeRMR, UnitType
# from IEC61970.Base.Generation.Production import CostPerHeatUnit
# from IEC61970.Base.Domain import ActivePower, CostRate, Integer, CostBasis, CostPerEnergyUnit
# from IEC62325.MarketOperations.ParticipantInterfaces import GeneratingBid, Trade, StartUpTimeCurve
# from IEC62325.MarketCommon import RegisteredResource


class RegisteredGenerator(RegisteredResource):
    """
    Model of a generator that is registered to participate in the market.
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        super().__init__()

        # The ratio of actual energy produced by resource divided by the maximum potential energy if the resource is
        # fully utilized. As an example, wind farms.
        self.capacity_factor = PerCent()

        # Cold start time.
        self.cold_start_time = 0.0

        # Combined Cycle operating mode.
        self.combined_cycle_operating_mode = ""

        # Commercial operation date.
        self.commericial_operation_date = DateTime()

        # Constrained Output Generator (COG) Indicator (Yes/No), per Generating Resource.
        self.constrained_output_flag = YesNo.NO

        # Response rate in MW per minute for ramping energy down.
        self.energy_down_ramp_rate = ActivePowerChangeRate()

        # Response rate in MW per minute for ramping energy up.
        self.energy_up_ramp_rate = ActivePowerChangeRate()

        # Some long-start uptime units may need to receive start up instruction before DA market results are
        # available. Long-Start resources may be either physical resources within the control with start-up times
        # greater than 18 hours or the long-start contractual inter-tie commitment that shall be completed by 6 am
        # one-day ahead. Therefore, there is a need for a process to determine the commitment of such resources
        # before the DA market.
        self.extreme_long_start = YesNo.NO

        # Values: Natural Gas Based Resource, Non Natural Gas Based Resource
        # "NG" - Natural-Gas-Based Resource - a Resource that is powered by Natural Gas
        # "NNG" - Non-Natural-Gas-Based Resource - a Resouce that is powered by some other fuel than Natural Gas
        self.fuel_source = FuelSource.GAS

        # High limit for secondary (AGC) control
        self.high_control_limit = ActivePower()

        # Hot-to-intermediate time (Seasonal)
        self.hot_int_time = 0.0

        # Hot start time.
        self.hot_start_time = 0.0

        # Intermediate-to-cold time (Seasonal)
        self.int_cold_time = 0.0

        # Intermediate start time.
        self.int_start_time = 0.0

        # Certifies resources for use in MSS Load Following Down
        self.load_following_down_mss = YesNo.NO

        # Certifies resources for use in MSS Load Following Up
        self.load_following_up_mss = YesNo.NO

        # Low limit for secondary (AGC) control
        self.low_control_limit = ActivePower()

        # Maximum Dependable Capacity (MNDC). Maximum Net Dependable Capacity is used in association with an RMR
        # contract.
        self.max_dependable_cap = ActivePower()

        # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value
        # regardless of the current operating point.
        self.maximum_allowable_spinning_reserve = ActivePower()

        # This is the maximum operating MW limit the dispatcher can enter for this unit
        self.maximum_operating_limit = ActivePower()

        # The registered maximum Minimum Load Cost of a Generating Resource registered with a Cost Basis of "Bid Cost".
        self.max_min_load_cost = CostRate()

        # Max pumping level of a hydro pump unit
        self.max_pumping_level = ActivePower()

        # Maximum time this device can be shut down.
        self.max_shutdown_time = DateTime()

        # Maximum start ups per day
        self.max_start_ups_per_day = 0

        # Maximum weekly Energy (Seasonal)
        self.max_weekly_energy = 0.0

        # Maximum weekly starts (seasonal parameter)
        self.max_weekly_starts = 0

        # The cost basis for minimum load.
        self.minimum_load_cost_basis = CostBasis.BIDC

        # The cost for the fuel required to get a Generating Resource to operate at the minimum load level
        self.minimum_load_fuel_cost = CostPerHeatUnit()

        # This is the minimum operating MW limit the dispatcher can enter for this unit.
        self.minimum_operating_limit = ActivePower()

        # Minimum load cost. Value is (currency/hr)
        self.min_load_cost = CostRate()

        # Flag to indicate that this unit is a resource adequacy resource and
        # adequacy resource and must offer.
        self.must_offer_ra = YesNo.NO

        # MW value stated on the nameplate of the Generator -- the value it potentially could provide.
        self.nameplate_capacity = ActivePower()

        # The portion of the Operating Cost of a Generating Resource that is not related to fuel cost.
        self.operating_maintenance_cost = CostPerEnergyUnit()

        # Pumping cost.
        self.pumping_cost = CostRate()

        # Pumping factor for pump storage units, conversion factor between generating and pumping.
        self.pumping_factor = 0.0

        # The minimum down time for the pump in a pump storage unit.
        self.pump_min_down_time = 0.0

        # The minimum up time aspect for the pump in a pump storage unit.
        self.pump_min_up_time = 0.0

        # The cost to shutdown a pump during the pump aspect of a pump storage unit.
        self.pump_shutdown_cost = 0.0

        # The shutdown time (minutes) of the pump aspect of a pump storage unit.
        self.pump_shutdown_time = 0

        # Quick start flag (Yes/No). Identifies the registered generator as a quick start unit. A quick start unit is
        # a unit that has the ability to be available for load within a 30 minute period.
        self.quick_start_flag = YesNo.NO

        # Ramp curve type. Identifies the type of curve which may be a fixed, static or dynamic.
        self.ramp_curve_type = RampCurveType.FIXED

        # Regulation down response rate in MW per minute.
        self.regulation_down_ramp_rate = ActivePowerChangeRate()

        # Specifies if the unit is regulating or not regulating or expected to be regulating but is not.
        self.regulation_flag = UnitRegulationKind.ONE

        # Regulation up response rate in MW per minute.
        self.regulation_up_ramp_rate = ActivePowerChangeRate()

        # Unit sub type used by Settlements or scheduling application. Application use of the unit sub type may
        # define the necessary types as applicable.
        self.resource_sub_type = ""

        # River System the Resource is tied to.
        self.river_system = ""

        # Reliability must not run (RMNR) flag: indicated whether the RMR unit is set as an RMNR in the current market.
        self.rmnr_flag = YesNo.NO

        # Reliability must run (RMR) flag: indicates whether the unit is RMR; Indicates whether the unit is RMR:
        # N' - not an RMR unit
        # '1' - RMR Condition 1 unit
        # '2' - RMR Condition 2 unit
        self.rmr_flag = FlagTypeRMR.N

        # Indicates the RMR Manual pre-determination status [Y/N].
        self.rmr_manual_indicator = YesNo.NO

        # Reliability must take (RMT) flag (Yes/No): indicates whether the unit is RMT.
        self.rmt_flag = YesNo.NO

        # Response rate in MW per minute for spinning reserve.
        self.spin_ramp_rate = ActivePowerChangeRate()

        # The cost basis for start up.
        self.start_up_cost_basis = CostBasis.BIDC

        # Is the Resource Synchronous Condenser capable Resource?
        self.sync_cond_capable = YesNo.NO

        # Generating unit type: Combined Cycle, Gas Turbine, Hydro Turbine, Other, Photovoltaic, Hydro Pump-Turbine,
        # Reciprocating Engine, Steam Turbine, Synchronous Condenser, Wind Turbine.
        self.unit_type = UnitType.COMBINED_CYCLE

        # Use limit flag: indicates if the use-limited resource is fully scheduled (or has some slack for real-time
        # dispatch) (Y/N).
        self.use_limit_flag = YesNo.NO

        # Provides an indication that this resource is intending to participate in an intermittent resource program.
        self.variable_energy_resource = YesNo.NO

        # RMR Heat Rate Curve.
        self.rmr_heat_rate_curve = None

        # RMR Start Up Fuel Curve.
        self.rmr_start_up_fuel_curve = None

        # Regulating Limit.
        self.regulating_limit = None

        # RMR Start Up Cost Curve.
        self.rmr_start_up_cost_curve = None

        # RMR Start Up Energy Curve.
        self.rmr_start_up_energy_curve = None

        # RMR Start Up Time Curve.
        self.rmr_start_up_time_curve = None

        # Start Up Fuel Curve.
        self.start_up_fuel_curve = None

        # Start Up Energy Curve.
        self.start_up_energy_curve = None

        # Mkt Heat Rate Curve.
        self.mkt_heat_rate_curve = None

        # Generating Bids.
        self.generating_bids = GeneratingBid()

        # Trade.
        self.trade = Trade()

        # Start Up Time Curve.
        self.start_up_time_curve = StartUpTimeCurve()
