package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.Resistance;
import TC57CIM.IEC61970.Base.Domain.Reactance;
import TC57CIM.IEC61970.Base.Core.IdentifiedObject;

/**
 * Transformer star impedance (Pi-model) that accurately reflects impedance for
 * transformers with 2 or 3 windings. For transformers with 4 or more windings,
 * you must use TransformerMeshImpedance class.
 * For transmission networks use PowerTransformerEnd impedances (r, r0, x, x0, b,
 * b0, g and g0).
 * @author T. Kostic
 * @version 1.0
 * @created 15-Dec-2023 4:38:30 PM
 */
public class TransformerStarImpedance extends IdentifiedObject {

	/**
	 * Resistance of the transformer end.
	 */
	public Resistance r;
	/**
	 * Zero sequence series resistance of the transformer end.
	 */
	public Resistance r0;
	/**
	 * Positive sequence series reactance of the transformer end.
	 */
	public Reactance x;
	/**
	 * Zero sequence series reactance of the transformer end.
	 */
	public Reactance x0;

	public TransformerStarImpedance(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}