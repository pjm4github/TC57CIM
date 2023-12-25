package TC57CIM.IEC61970.Base.DC;

import TC57CIM.IEC61970.Base.Core.ACDCTerminal;

/**
 * An electrical connection point at a piece of DC conducting equipment. DC
 * terminals are connected at one physical DC node that may have multiple DC
 * terminals connected. A DC node is similar to an AC connectivity node. The model
 * enforces that DC connections are distinct from AC connections.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class DCBaseTerminal extends ACDCTerminal {

	/**
	 * See association end Terminal.TopologicalNode.
	 */
	public DCTopologicalNode DCTopologicalNode;

	public DCBaseTerminal(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}