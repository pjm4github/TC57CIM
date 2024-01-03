package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Integer;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * Provides the necessary information (on a resource basis) to capture the
 * Dispatch Operating Target (DOT) results on a Dispatch interval. This
 * information is only relevant to the RT interval market.
 * @created 28-Dec-2023 8:20:05 PM
 */
public class DotInstruction {

	/**
	 * Actual ramp rate.
	 */
	public Float actualRampRate;
	/**
	 * Flag indicating whether or not the resource was in compliance with the
	 * instruction (plus/minus 10%).
	 * 
	 * Directs if a unit is allowed to set the price (ex-post pricing).
	 */
	public YesNo compliantIndicator;
	/**
	 * Dispatch operating target value.
	 */
	public Float DOT;
	/**
	 * Economic Max Limit override for unit, this value is null, if it is not, this
	 * value overrides the Energy column value.
	 * Allows dispatcher to override the unit's energy value.
	 */
	public Float economicMaxOverride;
	/**
	 * Expected energy.
	 */
	public Float expectedEnergy;
	/**
	 * The Degree of Generator Performance (DGP) used for the unit. Measure of how a
	 * generator responds to raise /lower signals.  Calculated every five minutes.
	 */
	public Float generatorPerformanceDegree;
	/**
	 * HASP results.
	 */
	public Float hourAheadSchedEnergy;
	/**
	 * Hourly Schedule (DA Energy Schedule).
	 */
	public Float hourlySchedule;
	/**
	 * The date/time for the instruction.
	 */
	public DateTime instructionTime;
	/**
	 * True if maximum emergency limit activated; false otherwise. If unit is
	 * requested  to move up to its max emergency limit., this flag is set to true.
	 */
	public Boolean maximumEmergencyInd;
	/**
	 * Meter Sub System Load Following. 
	 */
	public Float meterLoadFollowing;
	/**
	 * Desired MW that is not ramp restricted. If no ramp rate limit existed for the
	 * unit, this is the MW value tha t the unit was requested to move to.
	 */
	public Float nonRampRestrictedMW;
	/**
	 * Non Spin Reserve used to procure energy.
	 */
	public Float nonSpinReserve;
	/**
	 * Timestamp when the previous DOT value was issued.
	 */
	public DateTime previousDOTTimeStamp;
	/**
	 * The ramp rate limit for the unit in MWs per minute. Participant bidding data.
	 */
	public Float rampRateLimit;
	/**
	 * Regulation Status (Yes/No).
	 */
	public YesNo regulationStatus;
	/**
	 * Spin Reserve used to procure energy.
	 */
	public Float spinReserve;
	/**
	 * Standard ramping energy (MWH).
	 */
	public Float standardRampEnergy;
	/**
	 * Supplemental Energy procure by Real Time Dispatch.
	 */
	public Float supplementalEnergy;
	/**
	 * Output results from the case identifying the reason the unit was committed by
	 * the software.
	 */
	public Integer unitStatus;
	public RegisteredResource RegisteredResource;

	public DotInstruction(){

	}
}//end DotInstruction