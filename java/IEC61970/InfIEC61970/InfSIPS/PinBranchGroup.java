package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.OperationalLimits.BranchGroup;

/**
 * Value associated with branch group is used as compare.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:32:00 PM
 */
public class PinBranchGroup extends GateInputPin {

	/**
	 * The compare operation done on the branch group.
	 */
	public PinBranchGroupKind kind;
	public BranchGroup BranchGroup;

	public PinBranchGroup(){

	}
}//end PinBranchGroup