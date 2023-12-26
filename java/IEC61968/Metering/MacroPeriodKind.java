package IEC61968.Metering;


/**
 * Kind of macro period for calculations on read / measured values.
 * @author Marty
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public enum MacroPeriodKind {
	/**
	 * Not applicable.
	 */
	none,
	/**
	 * Captured during the billing period starting at midnight of the first day of the
	 * billing period (as defined by the billing cycle day). If during the current
	 * billing period, it specifies a period from the start of the current billing
	 * period until "now".
	 */
	billingPeriod,
	/**
	 * Daily period starting at midnight. If for the current day, this specifies the
	 * time from midnight to "now".
	 */
	daily,
	/**
	 * Monthly period starting at midnight on the first day of the month. If within
	 * the current month, this specifies the period from the start of the month until
	 * "now."
	 */
	monthly,
	/**
	 * A season of time spanning multiple months. E.g. "Summer," "Spring," "Fall," and
	 * "Winter" based cycle. If within the current season, it specifies the period
	 * from the start of the current season until "now."
	 */
	seasonal,
	/**
	 * Weekly period starting at midnight on the first day of the week and ending the
	 * instant before midnight the last day of the week. If within the current week,
	 * it specifies the period from the start of the week until "now."
	 */
	weekly,
	/**
	 * For the period defined by the start and end of the TimePeriod element in the
	 * message.
	 */
	specifiedPeriod
}