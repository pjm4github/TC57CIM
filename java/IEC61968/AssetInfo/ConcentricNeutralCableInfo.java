package IEC61968.AssetInfo;

import IEC61970.Base.Domain.Length;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.ResistancePerLength;

/**
 * Concentric neutral cable data.
 * @author Tom
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class ConcentricNeutralCableInfo extends CableInfo {

	/**
	 * Diameter over the concentric neutral strands.
	 */
	public Length diameterOverNeutral;
	/**
	 * Number of concentric neutral strands.
	 */
	public Integer neutralStrandCount;
	/**
	 * Geometric mean radius of the neutral strand.
	 */
	public Length neutralStrandGmr;
	/**
	 * Outside radius of the neutral strand.
	 */
	public Length neutralStrandRadius;
	/**
	 * DC resistance per unit length of the neutral strand at 20 øC.
	 */
	public ResistancePerLength neutralStrandRDC20;

	public ConcentricNeutralCableInfo(){

	}
}//end ConcentricNeutralCableInfo