package IEC61970.InfIEC61970.InfPart303.NetworkModelProjects;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Part303.GenericDataset.ChangeSet;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Describes the status and the planned implementation of the associated change
 * set into the as-built model.    New instances of this class with new identity
 * are instantiated upon changes to the content of this class or changes to the
 * associated change set.  Instances of this class are considered immutable.  The
 * case audit trail can reference this immutable data to exactly reproduce a case.
 * @author sveinols
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class NetworkModelProjectChangeVersion extends IdentifiedObject {

	/**
	 * A user provided comment describing the changes in this version from the
	 * previous version.
	 */
	public String comment;
	/**
	 * The date/time the change set is included in the model.
	 */
	public DateTime effectiveDateTime;
	/**
	 * The date/time this version was finalized and thus made immutable.
	 */
	public DateTime timeStamp;
	/**
	 * The details of model changes for this project.   The change set should have a
	 * new identifier if it changes.
	 */
	public ChangeSet ChangeSet;
	/**
	 * The persistent network model project change to which this version applies.
	 */
	public NetworkModelProjectChange NetworkModelProjectChange;
	/**
	 * The project version that will supercede this project version.
	 */
	public NetworkModelProjectChangeVersion SupercededBy;
	/**
	 * The state of this network model project version.
	 */
	public NetworkModelProjectState NetworkModelProjectState;

	public NetworkModelProjectChangeVersion(){

	}
}//end NetworkModelProjectChangeVersion