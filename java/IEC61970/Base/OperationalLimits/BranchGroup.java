package TC57CIM.IEC61970.Base.OperationalLimits;

import TC57CIM.IEC61970.Base.Domain.ActivePower;
import TC57CIM.IEC61970.Base.Domain.ReactivePower;
import TC57CIM.IEC61970.Base.Domain.Boolean;
import TC57CIM.IEC61970.Base.Core.IdentifiedObject;

/**
 * A group of branch terminals whose directed flow summation is to be monitored. A
 * branch group need not form a cutset of the network.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
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

	public void finalize() throws Throwable {
		super.finalize();
	}

}