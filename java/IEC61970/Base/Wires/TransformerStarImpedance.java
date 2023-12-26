package IEC61970.Base.Wires;

import IEC61970.Base.Domain.Resistance;
import IEC61970.Base.Domain.Reactance;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Transformer star impedance (Pi-model) that accurately reflects impedance for
 * transformers with 2 or 3 windings. For transformers with 4 or more windings,
 * you must use TransformerMeshImpedance class.
 * For transmission networks use PowerTransformerEnd impedances (r, r0, x, x0, b,
 * b0, g and g0).
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
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
}//end TransformerStarImpedance