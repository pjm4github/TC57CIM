package IEC61970.Base.OperationalLimits;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.ReactivePower;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A group of branch terminals whose directed flow summation is to be monitored. A
 * branch group need not form a cutset of the network.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class BranchGroup extends IdentifiedObject {

	/**
	 * The maximum active power flow.
	 */
	public ActivePower maximumActivePower;
	/**
	 * The maximum reactive power flow.
	 */
	public ReactivePower maximumReactivePower;
	/**
	 * The minimum active power flow.
	 */
	public ActivePower minimumActivePower;
	/**
	 * The minimum reactive power flow.
	 */
	public ReactivePower minimumReactivePower;
	/**
	 * Monitor the active power flow.
	 */
	public Boolean monitorActivePower;
	/**
	 * Monitor the reactive power flow.
	 */
	public Boolean monitorReactivePower;
	/**
	 * The directed branch group terminals to be summed.
	 */
	public BranchGroupTerminal BranchGroupTerminal;

	public BranchGroup(){

	}
}//end BranchGroup