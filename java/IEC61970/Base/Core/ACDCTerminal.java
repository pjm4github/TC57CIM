package TC57CIM.IEC61970.Base.Core;

import TC57CIM.IEC61970.Base.Domain.Boolean;
import TC57CIM.IEC61970.Base.Domain.Integer;

/**
 * An electrical connection point (AC or DC) to a piece of conducting equipment.
 * Terminals are connected at physical connection points called connectivity nodes.
 * 
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class ACDCTerminal extends IdentifiedObject {

	/**
	 * The connected status is related to a bus-branch model and the topological node
	 * to terminal relation.  True implies the terminal is connected to the related
	 * topological node and false implies it is not.
	 * In a bus-branch model, the connected status is used to tell if equipment is
	 * disconnected without having to change the connectivity described by the
	 * topological node to terminal relation. A valid case is that conducting
	 * equipment can be connected in one end and open in the other. In particular for
	 * an AC line segment, where the reactive line charging can be significant, this
	 * is a relevant case.
	 */
	public Boolean connected;
	/**
	 * The orientation of the terminal connections for a multiple terminal conducting
	 * equipment.  The sequence numbering starts with 1 and additional terminals
	 * should follow in increasing order.   The first terminal is the "starting point"
	 * for a two terminal branch.
	 */
	public Integer sequenceNumber;

	public ACDCTerminal(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}