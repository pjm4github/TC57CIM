package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Domain.ActivePowerChangeRate;
import IEC62325.MarketOperations.MktDomain.FuelSource;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.CostRate;
import IEC61970.Base.Domain.Integer;
import IEC62325.MarketOperations.MktDomain.CostBasis;
import IEC61970.Base.Generation.Production.CostPerHeatUnit;
import IEC61970.Base.Domain.CostPerEnergyUnit;
import IEC62325.MarketOperations.MktDomain.RampCurveType;
import IEC62325.MarketOperations.MktDomain.UnitRegulationKind;
import IEC62325.MarketOperations.MktDomain.FlagTypeRMR;
import IEC62325.MarketOperations.MktDomain.UnitType;
import IEC62325.MarketOperations.ParticipantInterfaces.GeneratingBid;
import IEC62325.MarketOperations.ParticipantInterfaces.Trade;
import IEC62325.MarketOperations.ParticipantInterfaces.StartUpTimeCurve;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * Model of a generator  that is registered to participate in the market.
 * @created 25-Dec-2023 8:48:38 PM
 */
public class RegisteredGenerator extends RegisteredResource {

	/**
	 * The ratio of actual energy produced by resource divided by the maximum
	 * potential energy if the resource is fully utilized. As an example, wind farms.
	 */
	public PerCent capacityFactor;
	/**
	 * Cold start time.
	 */
	public Float coldStartTime;
	/**
	 * Combined Cycle operating mode.
	 */
	public String combinedCycleOperatingMode;
	public DateTime commericialOperationDate;
	/**
	 * Constrained Output Generator (COG) Indicator (Yes/No), per Generating Resource
	 */
	public YesNo constrainedOutputFlag;
	/**
	 * Response rate in MW per minute for ramping energy down.
	 */
	public ActivePowerChangeRate energyDownRampRate;
	/**
	 * Response rate in MW per minute for ramping energy up.
	 */
	public ActivePowerChangeRate energyUpRampRate;
	/**
	 * Some long-start up time units may need to receive start up instruction before
	 * DA market results are available.  Long-Start resources may be either physical
	 * resources within the control with start-up times greater than 18 hours or the
	 * long-start contractual inter-tie commitment that shall be completed by 6 am one-
	 * day ahead.  Therefore, there is a need for a process to determine the
	 * commitment of such resources before the DA market.
	 */
	public YesNo extremeLongStart;
	/**
	 * Values: Natural Gas Based Resource, Non Natural Gas Based Resource
	 * "NG" - Natural-Gas-Based Resource - a Resource that is powered by Natural Gas
	 * "NNG" - Non-Natural-Gas-Based Resource - a Resouce that is powered by some
	 * other fuel than Natural Gas
	 */
	public FuelSource fuelSource;
	/**
	 * High limit for secondary (AGC) control
	 */
	public ActivePower highControlLimit;
	/**
	 * Hot-to-intermediate time (Seasonal)
	 */
	public Float hotIntTime;
	/**
	 * Hot start time.
	 */
	public Float hotStartTime;
	/**
	 * Intermediate-to-cold time (Seasonal)
	 */
	public Float intColdTime;
	/**
	 * Intermediate start time.
	 */
	public Float intStartTime;
	/**
	 * Certifies resources for use in MSS Load Following Down
	 */
	public YesNo loadFollowingDownMSS;
	/**
	 * Certifies resources for use in MSS Load Following Up
	 */
	public YesNo loadFollowingUpMSS;
	/**
	 * Low limit for secondary (AGC) control
	 */
	public ActivePower lowControlLImit;
	/**
	 * Maximum Dependable Capacity (MNDC). Maximun Net Dependable Capacity is used in
	 * association with an RMR contract.
	 */
	public ActivePower maxDependableCap;
	/**
	 * Maximum allowable spinning reserve. Spinning reserve will never be considered
	 * greater than this value regardless of the current operating point.
	 */
	public ActivePower maximumAllowableSpinningReserve;
	/**
	 * This is the maximum operating MW limit the dispatcher can enter for this unit
	 */
	public ActivePower maximumOperatingLimit;
	/**
	 * The registered maximum Minimum Load Cost of a Generating Resource registered
	 * with a Cost Basis of "Bid Cost".
	 */
	public CostRate maxMinLoadCost;
	/**
	 * max pumping level of a hydro pump unit
	 */
	public ActivePower maxPumpingLevel;
	/**
	 * Maximum time this device can be shut down.
	 */
	public DateTime maxShutdownTime;
	/**
	 * maximum start ups per day
	 */
	public Integer maxStartUpsPerDay;
	/**
	 * Maximum weekly Energy (Seasonal)
	 */
	public Float maxWeeklyEnergy;
	/**
	 * Maximum weekly starts (seasonal parameter)
	 */
	public Integer maxWeeklyStarts;
	/**
	 * The cost basis for minimum load.
	 */
	public CostBasis minimumLoadCostBasis;
	/**
	 * The cost for the fuel required to get a Generating Resource to operate at the
	 * minimum load level
	 */
	public CostPerHeatUnit minimumLoadFuelCost;
	/**
	 * This is the minimum operating MW limit the dispatcher can enter for this unit.
	 */
	public ActivePower minimumOperatingLimit;
	/**
	 * minimum load cost. Value is (currency/hr)
	 */
	public CostRate minLoadCost;
	/**
	 * Flag to indicate that this unit is a resource adequacy resource and must offer.
	 */
	public YesNo mustOfferRA;
	/**
	 * MW value stated on the nameplate of the Generator -- the value it potentially
	 * could provide.
	 */
	public ActivePower nameplateCapacity;
	/**
	 * The portion of the Operating Cost of a Generating Resource that is not related
	 * to fuel cost.
	 */
	public CostPerEnergyUnit operatingMaintenanceCost;
	public CostRate pumpingCost;
	/**
	 * Pumping factor for pump storage units, conversion factor between generating and
	 * pumping.
	 */
	public Float pumpingFactor;
	/**
	 * The minimum down time for the pump in a pump storage unit.
	 */
	public Float pumpMinDownTime;
	/**
	 * The minimum up time aspect for the pump in a pump storage unit
	 */
	public Float pumpMinUpTime;
	/**
	 * The cost to shutdown a pump during the pump aspect of a pump storage unit.
	 */
	public Float pumpShutdownCost;
	/**
	 * The shutdown time (minutes) of the pump aspect of a pump storage unit.
	 */
	public Integer pumpShutdownTime;
	/**
	 * Quick start flag (Yes/No). Identifies the registered generator as a quick start
	 * unit. A quick start unit is a unit that has the ability to be available for
	 * load within a 30 minute period.
	 */
	public YesNo quickStartFlag;
	/**
	 * Ramp curve type. Identifies the type of curve which may be a fixed, static or
	 * dynamic.
	 */
	public RampCurveType rampCurveType;
	/**
	 * Regulation down response rate in MW per minute
	 */
	public ActivePowerChangeRate regulationDownRampRate;
	/**
	 * Specifies if the unit is regulating or not regulating or expected to be
	 * regulating but is not.
	 */
	public UnitRegulationKind regulationFlag;
	/**
	 * Regulation up response rate in MW per minute.
	 */
	public ActivePowerChangeRate regulationUpRampRate;
	/**
	 * Unit sub type used by Settlements or scheduling application. Application use of
	 * the unit sub type may define the necessary types as applicable.
	 */
	public String resourceSubType;
	/**
	 * River System the Resource is tied to.
	 */
	public String riverSystem;
	/**
	 * Reliability must not run (RMNR) flag: indicated whether the RMR unit is set as
	 * an RMNR in the current market
	 */
	public YesNo RMNRFlag;
	/**
	 * Reliability must run (RMR) flag: indicates whether the unit is RMR; Indicates
	 * whether the unit is RMR:
	 * N' - not an RMR unit
	 * '1' - RMR Condition 1 unit
	 * '2' - RMR Condition 2 unit
	 */
	public FlagTypeRMR RMRFlag;
	/**
	 * Indicates the RMR Manual pre-determination status [Y/N]
	 */
	public YesNo RMRManualIndicator;
	/**
	 * Reliability must take (RMT) flag (Yes/No): indicates whether the unit is RMT
	 */
	public YesNo RMTFlag;
	/**
	 * Response rate in MW per minute for spinning reserve.
	 */
	public ActivePowerChangeRate spinRampRate;
	/**
	 * The cost basis for start up.
	 */
	public CostBasis startUpCostBasis;
	/**
	 * Is the Resource Synchronous Condenser capable Resource? 
	 */
	public YesNo syncCondCapable;
	/**
	 * Generating unit type: Combined Cycle, Gas Turbine, Hydro Turbine, Other,
	 * Photovoltaic, Hydro Pump-Turbine, Reciprocating Engine, Steam Turbine,
	 * Synchronous Condenser, Wind Turbine
	 */
	public UnitType unitType;
	/**
	 * Use limit flag: indicates if the use-limited resource is fully scheduled (or
	 * has some slack for real-time dispatch) (Y/N)
	 */
	public YesNo useLimitFlag;
	/**
	 * Provides an indication that this resource is intending to participate in an
	 * intermittent resource program.
	 */
	public YesNo variableEnergyResource;
	public RMRHeatRateCurve RMRHeatRateCurve;
	public RMRStartUpFuelCurve RMRStartUpFuelCurve;
	public RegulatingLimit RegulatingLimit;
	public RMRStartUpCostCurve RMRStartUpCostCurve;
	public RMRStartUpEnergyCurve RMRStartUpEnergyCurve;
	public RMRStartUpTimeCurve RMRStartUpTimeCurve;
	public StartUpFuelCurve StartUpFuelCurve;
	public StartUpEnergyCurve StartUpEnergyCurve;
	public MktHeatRateCurve MktHeatRateCurve;
	public GeneratingBid GeneratingBids;
	public Trade Trade;
	public StartUpTimeCurve StartUpTimeCurve;

	public RegisteredGenerator(){

	}
}//end RegisteredGenerator