package IEC61970.Base.OperationalLimits;


/**
 * The direction attribute describes the side of  a limit that is a violation.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public enum OperationalLimitDirectionKind {
	/**
	 * High means that a monitored value above the limit value is a violation.   If
	 * applied to a terminal flow, the positive direction is into the terminal.
	 */
	high,
	/**
	 * Low means a monitored value below the limit is a violation.  If applied to a
	 * terminal flow, the positive direction is into the terminal.
	 */
	low,
	/**
	 * An absoluteValue limit means that a monitored absolute value above the limit
	 * value is a violation.
	 */
	absoluteValue
}