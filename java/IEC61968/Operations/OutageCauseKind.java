package IEC61968.Operations;


/**
 * This enumeration describes the primary cause of the outage - planned, unplanned,
 * etc.
 * @author Margaret
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public enum OutageCauseKind {
	lightingStrike,
	/**
	 * This outage was caused by an animal is was unplanned.  As such it is treated as
	 * a forced outage and is probably classified as "trouble" with a Trouble Ticket
	 * as well as a work/service order.  The primary difference between this and an
	 * unplanned outage is the reason for the outage.  If an animal caused this and
	 * perished as a result, the utility may have other actions that are required to
	 * be taken by the EPA or other groups with whom the utility has an agreement.
	 */
	animal,
	lineDown,
	poleDown,
	treeDown
}