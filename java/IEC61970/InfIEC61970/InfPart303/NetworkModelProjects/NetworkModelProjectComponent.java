package IEC61970.InfIEC61970.InfPart303.NetworkModelProjects;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * Abstract class for both a network model project and network model change.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class NetworkModelProjectComponent extends IdentifiedObject {

	public NetworkModelProjectDocument m_NetworkModelProjectDocument;
	/**
	 * The parent project of this project.
	 */
	public NetworkModelProject ContainingProject;

	public NetworkModelProjectComponent(){

	}
}//end NetworkModelProjectComponent

/**
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class NetworkModelProjectComponent extends IdentifiedObject {

	public DateTime closed;
	public DateTime created;
	public DateTime updated;
	public int version;
	public CurrentState m_CurrentState;
	public NetworkModelProject2 Parent;

	public NetworkModelProjectComponent(){

	}
}//end NetworkModelProjectComponent