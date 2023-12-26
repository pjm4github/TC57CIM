package IEC62325.MarketManagement;

import IEC61970.Base.Domain.Duration;
import IEC61970.Base.Domain.String;

/**
 * Duration constraint to activate, to put in operation, to deactivate, ... a
 * given event.
 * @author ENTSOE
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class ConstraintDuration {

	/**
	 * The duration of the constraint.
	 */
	public Duration duration;
	/**
	 * The type of the constraint.
	 */
	public String type;
	public TimeSeries TimeSeries;

	public ConstraintDuration(){

	}
}//end ConstraintDuration