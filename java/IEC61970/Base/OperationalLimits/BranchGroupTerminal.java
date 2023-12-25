package TC57CIM.IEC61970.Base.OperationalLimits;

import TC57CIM.IEC61970.Base.Domain.Boolean;
import TC57CIM.IEC61970.Base.Core.Terminal;

/**
 * A specific directed terminal flow for a branch group.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class BranchGroupTerminal {

	/**
	 * The flow into the terminal is summed if set true.   The flow out of the
	 * terminanl is summed if set false.
	 */
	public Boolean positiveFlowIn;
	/**
	 * The terminal to be summed.
	 */
	public Terminal Terminal;

	public BranchGroupTerminal(){

	}

	public void finalize() throws Throwable {

	}

}