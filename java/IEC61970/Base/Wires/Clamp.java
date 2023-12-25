package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.Length;
import TC57CIM.IEC61970.Base.Core.ConductingEquipment;

/**
 * A Clamp is a galvanic connection at a line segment where other equipment is
 * connected. A Clamp does not cut the line segment.
 * A Clamp is ConductingEquipment and has one Terminal with an associated
 * ConnectivityNode. Any other ConductingEquipment can be connected to the Clamp
 * ConnectivityNode.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class Clamp extends ConductingEquipment {

	/**
	 * The length to the place where the clamp is located starting from side one of
	 * the line segment, i.e. the line segment terminal with sequence number equal to
	 * 1.
	 */
	public Length lengthFromTerminal1;

	public Clamp(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}