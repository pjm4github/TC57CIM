package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * Logical gate than support logical operation based on the input.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:30:06 PM
 */
public class Gate extends IdentifiedObject {

	/**
	 * The logical operation of the gate.
	 */
	public GateLogicKind kind;
	public RemedialActionScheme RemedialActionScheme;
	public PinGate PinGate;
	public GateInputPin GateInputPin;

	public Gate(){

	}
}//end Gate