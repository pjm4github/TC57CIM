package IEC61970.Part552Header.DifferenceModel;

import IEC61970.Part552Header.ModelDescription.Model;
import IEC61970.Part552Header.Statements;
import IEC61970.InfIEC61970.InfPart303.NetworkModelProjects.NetworkModelProjectChangeVersion;

/**
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class DifferenceModel extends Model {

	public Statements reverseDifferences;
	public Statements forwardDifferences;
	public NetworkModelProjectChangeVersion m_NetworkModelProjectChangeVersion;

	public DifferenceModel(){

	}
}//end DifferenceModel