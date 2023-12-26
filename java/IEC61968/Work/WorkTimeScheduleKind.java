package IEC61968.Work;


/**
 * Kind of work schedule.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:26 PM
 */
public enum WorkTimeScheduleKind {
	/**
	 * Estimate work time schedule.
	 */
	estimate,
	/**
	 * Request work time schedule.
	 */
	request,
	/**
	 * Actual work time schedule.
	 */
	actual,
	/**
	 * Earliest work time schedule.
	 */
	earliest,
	/**
	 * Latest work time schedule.
	 */
	latest,
	immediate
}