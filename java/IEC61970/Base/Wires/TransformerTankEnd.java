package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Core.PhaseCode;

/**
 * Transformer tank end represents an individual winding for unbalanced models or
 * for transformer tanks connected into a bank (and bank is modelled with the
 * PowerTransformer).
 * @author T. Kostic
 * @version 1.0
 * @created 15-Dec-2023 4:38:30 PM
 */
public class TransformerTankEnd extends TransformerEnd {

	/**
	 * Describes the phases carried by a conducting equipment.
	 */
	public PhaseCode phases;
	/**
	 * Transformer this winding belongs to.
	 */
	public TransformerTank TransformerTank;

	public TransformerTankEnd(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}