package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Core.Terminal;

/**
 * Value associated with Terminal is used as compare.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:33:05 PM
 */
public class PinTerminal extends GateInputPin {

	/**
	 * The compare operation done on the terminal.
	 */
	public PinTerminalKind kind;
	public Terminal Terminal;

	public PinTerminal(){

	}
}//end PinTerminal