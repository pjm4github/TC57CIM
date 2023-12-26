package IEC62325.Environmental.EnvDomain;


/**
 * Method by which information is gathered from station.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public enum ReportingMethodKind {
	/**
	 * Station automatically reports.
	 */
	automated,
	/**
	 * Station must be queried to obtain observations.
	 */
	queried,
	/**
	 * Station must be physically visited to gather observations.
	 */
	manual
}