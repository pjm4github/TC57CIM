package IEC61968.Operations;


/**
 * The estimated time of restoration can have a confidence factor applied such as
 * high or low confidence that the ERT will be accomplished.  This confidence
 * factor may be updated as needed during the outage period - just as the actual
 * ERT can be updated.
 * @author Margaret
 * @version 1.0
 * @created 25-Dec-2023 8:45:21 PM
 */
public enum ERTConfidenceKind {
	/**
	 * there is a high confidence that the ERT will be accomplished
	 */
	high,
	/**
	 * there is a low confidence that the ERT will be accomplished.
	 */
	low
}