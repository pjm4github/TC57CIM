package IEC61970.InfIEC61970.InfPart303.NetworkModelFrames;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * A description for how to assemble model parts for a specific purpose.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class AssemblyDescription extends IdentifiedObject {

	/**
	 * The models that are part of the assembly descrption.
	 */
	private ModelPartSpecification ModelSpecification;

	public AssemblyDescription(){

	}
}//end AssemblyDescription