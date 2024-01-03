package IEC61970.Base.Meas;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.SCADA.Source;

/**
 * Quality flags in this class are as defined in IEC 61850, except for
 * estimatorReplaced, which has been included in this class for convenience.
 * @updated 02-Jan-2024 11:24:58 PM
 */
public class Quality61850 {

	/**
	 * Measurement value may be incorrect due to a reference being out of calibration.
	 */
	public Boolean badReference;
	/**
	 * Value has been replaced by State Estimator. estimatorReplaced is not an
	 * IEC61850 quality bit but has been put in this class for convenience.
	 */
	public Boolean estimatorReplaced;
	/**
	 * This identifier indicates that a supervision function has detected an internal
	 * or external failure, e.g. communication failure.
	 */
	public Boolean failure;
	/**
	 * Measurement value is old and possibly invalid, as it has not been successfully
	 * updated during a specified time interval.
	 */
	public Boolean oldData;
	/**
	 * Measurement value is blocked and hence unavailable for transmission. 
	 */
	public Boolean operatorBlocked;
	/**
	 * To prevent some overload of the communication it is sensible to detect and
	 * suppress oscillating (fast changing) binary inputs. If a signal changes in a
	 * defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0)
	 * then oscillation is detected and the detail quality identifier "oscillatory" is
	 * set. If it is detected a configured numbers of transient changes could be
	 * passed by. In this time the validity status "questionable" is set. If after
	 * this defined numbers of changes the signal is still in the oscillating state
	 * the value shall be set either to the opposite state of the previous stable
	 * value or to a defined default value. In this case the validity status
	 * "questionable" is reset and "invalid" is set as long as the signal is
	 * oscillating. If it is configured such that no transient changes should be
	 * passed by then the validity status "invalid" is set immediately in addition to
	 * the detail quality identifier "oscillatory" (used for status information only).
	 */
	public Boolean oscillatory;
	/**
	 * Measurement value is beyond a predefined range of value.
	 */
	public Boolean outOfRange;
	/**
	 * Measurement value is beyond the capability of being  represented properly. For
	 * example, a counter value overflows from maximum count back to a value of zero. 
	 */
	public Boolean overFlow;
	/**
	 * Source gives information related to the origin of a value. The value may be
	 * acquired from the process, defaulted or substituted.
	 */
	public Source source;
	/**
	 * A correlation function has detected that the value is not consitent with other
	 * values. Typically set by a network State Estimator.
	 */
	public Boolean suspect;
	/**
	 * Measurement value is transmitted for test purposes.
	 */
	public Boolean test;
	/**
	 * Validity of the measurement value.
	 */
	public Validity validity;

	public Quality61850(){

	}
}//end Quality61850