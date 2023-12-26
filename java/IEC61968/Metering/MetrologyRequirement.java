package IEC61968.Metering;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * A specification of the metering requirements for a particular point within a
 * network.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class MetrologyRequirement extends IdentifiedObject {

	/**
	 * Reason for this metrology requirement being specified.
	 */
	public ReadingReasonKind reason;
	/**
	 * All usage points having this metrology requirement.
	 */
	public UsagePoint UsagePoints;
	/**
	 * All reading types required to be collected by this metrology requirement.
	 */
	public ReadingType ReadingTypes;

	public MetrologyRequirement(){

	}
}//end MetrologyRequirement