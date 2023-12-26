package IEC61970.InfIEC61970.InfPart303.NetworkModelProjects;

import IEC61970.Part303.GenericDataset.ChangeSet;

/**
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class NetworkModelProjectStage extends NetworkModelProjectComponent {

	public int changesetVersion;
	public DateTime commissionedDate;
	public DateTime plannedCommissionedDate;
	public ChangeSet m_ChangeSet;

	public NetworkModelProjectStage(){

	}
}//end NetworkModelProjectStage