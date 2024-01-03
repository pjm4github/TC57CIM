package IEC61970.Base.Core;

import IEC61970.Base.Wires.RegulatingControl;

/**
 * An AC electrical connection point to a piece of conducting equipment. Terminals
 * are connected at physical connection points called connectivity nodes.
 * @created 02-Jan-2024 10:38:11 PM
 */
public class Terminal extends ACDCTerminal {

	/**
	 * Represents the normal network phasing condition.
	 * If the attribute is missing three phases (ABC or ABCN) shall be assumed.
	 */
	public PhaseCode phases;
	/**
	 * The connectivity node to which this terminal connects with zero impedance.
	 */
	public ConnectivityNode ConnectivityNode;
	/**
	 * The conducting equipment of the terminal.  Conducting equipment have  terminals
	 * that may be connected to other conducting equipment terminals via connectivity
	 * nodes or topological nodes.
	 */
	public ConductingEquipment ConductingEquipment;
	/**
	 * The controls regulating this terminal.
	 */
	public RegulatingControl RegulatingControl;

	public Terminal(){

	}
}//end Terminal