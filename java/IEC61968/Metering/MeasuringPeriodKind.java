package IEC61968.Metering;


/**
 * Kind of period for reading / measuring values.
 * @author Marty
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public enum MeasuringPeriodKind {
	/**
	 * Not applicable.
	 */
	none,
	/**
	 * 10-minute
	 */
	tenMinute,
	/**
	 * 15-minute
	 */
	fifteenMinute,
	/**
	 * 1-minute
	 */
	oneMinute,
	/**
	 * 24-hour
	 */
	twentyfourHour,
	/**
	 * 30-minute
	 */
	thirtyMinute,
	/**
	 * 5-minute
	 */
	fiveMinute,
	/**
	 * 60-minute
	 */
	sixtyMinute,
	/**
	 * 2-minute
	 */
	twoMinute,
	/**
	 * 3-minute
	 */
	threeMinute,
	/**
	 * Within the present period of time
	 */
	present,
	/**
	 * Shifted within the previous monthly cycle and data set
	 */
	previous,
	/**
	 * 20-minute interval
	 */
	twentyMinute,
	/**
	 * 60-minute Fixed Block
	 */
	fixedBlock60Min,
	/**
	 * 30-minute Fixed Block
	 */
	fixedBlock30Min,
	/**
	 * 20-minute Fixed Block
	 */
	fixedBlock20Min,
	/**
	 * 15-minute Fixed Block
	 */
	fixedBlock15Min,
	/**
	 * 10-minute Fixed Block
	 */
	fixedBlock10Min,
	/**
	 * 5-minute Fixed Block
	 */
	fixedBlock5Min,
	/**
	 * 1-minute Fixed Block
	 */
	fixedBlock1Min,
	/**
	 * 60-minute Rolling Block with 30-minute sub-intervals
	 */
	rollingBlock60MinIntvl30MinSubIntvl,
	/**
	 * 60-minute Rolling Block with 20-minute sub-intervals
	 */
	rollingBlock60MinIntvl20MinSubIntvl,
	/**
	 * 60-minute Rolling Block with 15-minute sub-intervals
	 */
	rollingBlock60MinIntvl15MinSubIntvl,
	/**
	 * 60-minute Rolling Block with 12-minute sub-intervals
	 */
	rollingBlock60MinIntvl12MinSubIntvl,
	/**
	 * 60-minute Rolling Block with 10-minute sub-intervals
	 */
	rollingBlock60MinIntvl10MinSubIntvl,
	/**
	 * 60-minute Rolling Block with 6-minute sub-intervals
	 */
	rollingBlock60MinIntvl6MinSubIntvl,
	/**
	 * 60-minute Rolling Block with 5-minute sub-intervals
	 */
	rollingBlock60MinIntvl5MinSubIntvl,
	/**
	 * 60-minute Rolling Block with 4-minute sub-intervals
	 */
	rollingBlock60MinIntvl4MinSubIntvl,
	/**
	 * 30-minute Rolling Block with 15-minute sub-intervals
	 */
	rollingBlock30MinIntvl15MinSubIntvl,
	/**
	 * 30-minute Rolling Block with 10-minute sub-intervals
	 */
	rollingBlock30MinIntvl10MinSubIntvl,
	/**
	 * 30-minute Rolling Block with 6-minute sub-intervals
	 */
	rollingBlock30MinIntvl6MinSubIntvl,
	/**
	 * 30-minute Rolling Block with 5-minute sub-intervals.
	 */
	rollingBlock30MinIntvl5MinSubIntvl,
	/**
	 * 30-minute Rolling Block with 3-minute sub-intervals
	 */
	rollingBlock30MinIntvl3MinSubIntvl,
	/**
	 * 30-minute Rolling Block with 2-minute sub-intervals
	 */
	rollingBlock30MinIntvl2MinSubIntvl,
	/**
	 * 15-minute Rolling Block with 5-minute sub-intervals
	 */
	rollingBlock15MinIntvl5MinSubIntvl,
	/**
	 * 15-minute Rolling Block with 3-minute sub-intervals
	 */
	rollingBlock15MinIntvl3MinSubIntvl,
	/**
	 * 15-minute Rolling Block with 1-minute sub-intervals
	 */
	rollingBlock15MinIntvl1MinSubIntvl,
	/**
	 * 10-minute Rolling Block with 5-minute sub-intervals
	 */
	rollingBlock10MinIntvl5MinSubIntvl,
	/**
	 * 10-minute Rolling Block with 2-minute sub-intervals
	 */
	rollingBlock10MinIntvl2MinSubIntvl,
	/**
	 * 10-minute Rolling Block with 1-minute sub-intervals
	 */
	rollingBlock10MinIntvl1MinSubIntvl,
	/**
	 * 5-minute Rolling Block with 1-minute sub-intervals
	 */
	rollingBlock5MinIntvl1MinSubIntvl
}