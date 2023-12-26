package IEC61968.Operations;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;
import IEC61968.Work.WorkTask;
import IEC61968.Common.Document;

/**
 * A sequence of grouped or atomic steps intended to:
 * - de-energise equipment or part of the network for safe work, and/or
 * - bring back in service previously de-energised equipment or part of the
 * network.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class SwitchingPlan extends Document {

	/**
	 * The date and time the switching plan was approved
	 */
	public DateTime approvedDateTime;
	/**
	 * Date and Time the switching plan was cancelled.
	 */
	public DateTime cancelledDateTime;
	/**
	 * the planned start and end times for the switching plan.
	 */
	public DateTimeInterval plannedPeriod;
	/**
	 * Purpose of  this plan, such as whether it is to move the state from normal to
	 * some abnormal condition, or to restore the normal state after an abnormal
	 * condition, or to perform some kind of optimisation such as correction of
	 * overload, voltage control, etc.
	 */
	public String purpose;
	/**
	 * Ranking in comparison to other switching plans.
	 */
	public Integer rank;
	/**
	 * Outage that will be activated or eliminated when this switching plan gets
	 * executed.
	 */
	public Outage Outage;
	/**
	 * All groups of switching steps within this switching plan.
	 */
	public SwitchingStepGroup SwitchingStepGroups;
	/**
	 * All safety documents applicable to this swtiching plan.
	 */
	public SafetyDocument SafetyDocuments;
	/**
	 * The outage plan for which the switching plan is defined.
	 */
	public OutagePlan OutagePlan;
	/**
	 * All work tasks to execute this switching plan.
	 */
	public WorkTask WorkTasks;

	public SwitchingPlan(){

	}
}//end SwitchingPlan