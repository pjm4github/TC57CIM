package IEC61968.AssetInfo;

import IEC61970.Base.Wires.WindingConnection;
import IEC61970.Base.Domain.ApparentPower;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.Resistance;
import IEC61970.Base.Wires.TransformerCoreAdmittance;
import IEC61970.Base.Wires.TransformerMeshImpedance;
import IEC61970.Base.Wires.TransformerStarImpedance;
import IEC61968.Assets.AssetInfo;

/**
 * Transformer end data.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class TransformerEndInfo extends AssetInfo {

	/**
	 * Kind of connection.
	 */
	public WindingConnection connectionKind;
	/**
	 * Apparent power that the winding can carry under emergency conditions (also
	 * called long-term emergency power).
	 */
	public ApparentPower emergencyS;
	/**
	 * Number for this transformer end, corresponding to the end's order in the
	 * PowerTransformer.vectorGroup attribute. Highest voltage winding should be 1.
	 */
	public Integer endNumber;
	/**
	 * Basic insulation level voltage rating.
	 */
	public Voltage insulationU;
	/**
	 * Winding phase angle where 360 degrees are represented with clock hours, so the
	 * valid values are {0, ..., 11}. For example, to express the second winding in
	 * code 'Dyn11', set attributes as follows: 'endNumber'=2, 'connectionKind' = Yn
	 * and 'phaseAngleClock' = 11.
	 */
	public Integer phaseAngleClock;
	/**
	 * DC resistance.
	 */
	public Resistance r;
	/**
	 * Normal apparent power rating.
	 */
	public ApparentPower ratedS;
	/**
	 * Rated voltage: phase-phase for three-phase windings, and either phase-phase or
	 * phase-neutral for single-phase windings.
	 */
	public Voltage ratedU;
	/**
	 * Apparent power that this winding can carry for a short period of time (in
	 * emergency).
	 */
	public ApparentPower shortTermS;
	/**
	 * Core admittance calculated from this transformer end datasheet, representing
	 * magnetising current and core losses. The full values of the transformer should
	 * be supplied for one transformer end info only.
	 */
	public TransformerCoreAdmittance CoreAdmittance;
	/**
	 * All mesh impedances between this 'to' and other 'from' transformer ends.
	 */
	public TransformerMeshImpedance FromMeshImpedances;
	/**
	 * Transformer star impedance calculated from this transformer end datasheet.
	 */
	public TransformerStarImpedance TransformerStarImpedance;
	/**
	 * All mesh impedances between this 'from' and other 'to' transformer ends.
	 */
	public TransformerMeshImpedance ToMeshImpedances;

	public TransformerEndInfo(){

	}
}//end TransformerEndInfo