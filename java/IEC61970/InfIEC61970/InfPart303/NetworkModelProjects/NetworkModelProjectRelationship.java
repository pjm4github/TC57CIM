package IEC61970.InfIEC61970.InfPart303.NetworkModelProjects;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * A relationship that assists humans and software building cases by assembling
 * project changes in the correct sequence.  This class may be specialized to
 * create specific types of relationships.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public abstract class NetworkModelProjectRelationship extends IdentifiedObject {

	public NetworkModelProjectComponent ProjectA;
	public NetworkModelProjectComponent ProjectB;

	public NetworkModelProjectRelationship(){

	}
}//end NetworkModelProjectRelationship