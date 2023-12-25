package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Core.Equipment;

/**
 * An assembly of two or more coupled windings that transform electrical power
 * between voltage levels. These windings are bound on a common core and place in
 * the same tank. Transformer tank can be used to model both single-phase and 3-
 * phase transformers.
 * @author Tom
 * @version 1.0
 * @created 15-Dec-2023 4:38:30 PM
 */
public class TransformerTank extends Equipment {

	/**
	 * Bank this transformer belongs to.
	 */
	public PowerTransformer PowerTransformer;

	public TransformerTank(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}