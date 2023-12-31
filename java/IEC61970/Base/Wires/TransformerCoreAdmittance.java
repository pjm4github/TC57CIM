package IEC61970.Base.Wires;

import IEC61970.Base.Domain.Susceptance;
import IEC61970.Base.Domain.Conductance;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * The transformer core admittance.  Used to specify the core admittance of a
 * transformer in a manner that can be shared among power transformers.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class TransformerCoreAdmittance extends IdentifiedObject {

	/**
	 * Magnetizing branch susceptance (B mag).  The value can be positive or negative.
	 */
	public Susceptance b;
	/**
	 * Zero sequence magnetizing branch susceptance.
	 */
	public Susceptance b0;
	/**
	 * Magnetizing branch conductance (G mag).
	 */
	public Conductance g;
	/**
	 * Zero sequence magnetizing branch conductance.
	 */
	public Conductance g0;
	/**
	 * All transformer ends having this core admittance.
	 */
	public TransformerEnd TransformerEnd;

	public TransformerCoreAdmittance(){

	}
}//end TransformerCoreAdmittance