package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.ActivePowerChangeRate;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Integer;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.SecurityConstraints;

/**
 * Offer to supply energy/ancillary services from a generating unit or resource.
 * @created 28-Dec-2023 5:21:13 PM
 */
public class GeneratingBid extends ResourceBid {

	/**
	 * Will indicate if the unit is part of a CC offer or not
	 */
	public String combinedCycleUnitOffer;
	/**
	 * Maximum down time.
	 */
	public Float downTimeMax;
	/**
	 * Installed Capacity value
	 */
	public Float installedCapacity;
	/**
	 * Maximum Dn ramp rate in MW/min
	 */
	public ActivePowerChangeRate lowerRampRate;
	/**
	 * Power rating available for unit under emergency conditions greater than or
	 * equal to maximum economic limit.
	 */
	public ActivePower maxEmergencyMW;
	/**
	 * Maximum high economic MW limit, that should not exceed the maximum operating MW
	 * limit
	 */
	public Float maximumEconomicMW;
	/**
	 * Minimum power rating for unit under emergency conditions, which is less than or
	 * equal to the economic minimum.
	 */
	public ActivePower minEmergencyMW;
	/**
	 * Low economic MW limit that shall be greater than or equal to the minimum
	 * operating MW limit
	 */
	public Float minimumEconomicMW;
	/**
	 * Resource fixed no load cost.
	 */
	public Float noLoadCost;
	/**
	 * Time required for crew notification prior to start up of the unit.
	 */
	public Float notificationTime;
	/**
	 * Bid operating mode ('C' - cycling, 'F' - fixed, 'M' - must run, 'U' -
	 * unavailable)
	 */
	public String operatingMode;
	/**
	 * Maximum Up ramp rate in MW/min
	 */
	public ActivePowerChangeRate raiseRampRate;
	/**
	 * Ramp curve type:
	 * 0 - Fixed ramp rate independent of rate function unit MW output
	 * 1 - Static ramp rates as a function of unit MW output only
	 * 2 - Dynamic ramp rates as a function of unit MW output and ramping time
	 */
	public Integer rampCurveType;
	/**
	 * Startup cost/price
	 */
	public Float startupCost;
	/**
	 * Resource startup ramp rate (MW/minute)
	 */
	public ActivePowerChangeRate startUpRampRate;
	/**
	 * Resource startup type:
	 * 1 - Fixed startup time and fixed startup cost
	 * 2 - Startup time as a function of down time and fixed startup cost
	 * 3 - Startup cost as a function of down time
	 */
	public Integer startUpType;
	/**
	 * Maximum up time.
	 */
	public Float upTimeMax;
	public NotificationTimeCurve NotificationTimeCurve;
	public RampRateCurve RampRateCurve;
	public SecurityConstraints SecurityConstraints;

	public GeneratingBid(){

	}
}//end GeneratingBid