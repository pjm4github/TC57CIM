package IEC62325.InfIEC62325.InfFinancial;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Agreement;

/**
 * A type of agreement that provides the default method by which interchange
 * schedules are to be integrated to obtain hourly MWh schedules for accounting.
 * @created 03-Jan-2024 1:52:02 PM
 */
public class IntSchedAgreement extends Agreement {

	/**
	 * The default method by which interchange schedules are to be integrated to
	 * obtain hourly MWh schedules for accounting. Method #1 is to integrate the
	 * instantaneous schedule between the hourly boundaries. Method #2 compensates for
	 * any up/down ramping that occurs across the hourly boundary (this is called
	 * block accounting).
	 */
	public String defaultIntegrationMethod;

	public IntSchedAgreement(){

	}
}//end IntSchedAgreement