package IEC61970.InfIEC61970.InfPart303.NetworkModelProjects;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class AnnotatedProjectDependency extends IdentifiedObject {

	public DependencyType dependencyType;
	public NetworkModelProjectStage DependentOnStage;
	public NetworkModelProjectStage DependingStage;

	public AnnotatedProjectDependency(){

	}
}//end AnnotatedProjectDependency