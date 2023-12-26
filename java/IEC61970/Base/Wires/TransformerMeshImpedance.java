package IEC61970.Base.Wires;

import IEC61970.Base.Domain.Resistance;
import IEC61970.Base.Domain.Reactance;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Transformer mesh impedance (Delta-model) between transformer ends.
 * The typical case is that this class describes the impedance between two
 * transformer ends pair-wise, i.e. the cardinalities at both tranformer end
 * associations are 1. But in cases where two or more transformer ends are modeled
 * the cardinalities are larger than 1.
 * @author LOO
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class TransformerMeshImpedance extends IdentifiedObject {

	/**
	 * Resistance between the 'from' and the 'to' end, seen from the 'from' end.
	 */
	public Resistance r;
	/**
	 * Zero-sequence resistance between the 'from' and the 'to' end, seen from the
	 * 'from' end.
	 */
	public Resistance r0;
	/**
	 * Reactance between the 'from' and the 'to' end, seen from the 'from' end.
	 */
	public Reactance x;
	/**
	 * Zero-sequence reactance between the 'from' and the 'to' end, seen from the
	 * 'from' end.
	 */
	public Reactance x0;
	/**
	 * All transformer ends this mesh impedance is connected to.
	 */
	public TransformerEnd ToTransformerEnd;
	/**
	 * From end this mesh impedance is connected to. It determines the voltage
	 * reference.
	 */
	public TransformerEnd FromTransformerEnd;

	public TransformerMeshImpedance(){

	}
}//end TransformerMeshImpedance