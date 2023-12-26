package IEC61968.Operations;

import IEC61970.Base.Domain.String;

/**
 * The Estimated Restoration Time for a single outage
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:21 PM
 */
public class EstimatedRestorationTime {

	/**
	 * provides the confidence level that this ERT can be accomplished.  This may be
	 * changed/updated as needed.
	 */
	public ERTConfidenceKind confidenceKind;
	/**
	 * estimated time the outage will be restored
	 */
	public EstimatedRestorationTime ert;
	/**
	 * defines the source that provided the ERT value.
	 */
	public String ertSource;
	public Outage Outage;

	public EstimatedRestorationTime(){

	}
}//end EstimatedRestorationTime