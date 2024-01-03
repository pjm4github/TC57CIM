package IEC61968.AssetInfo;

import IEC61970.Base.Domain.Length;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.ResistancePerLength;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.String;
import IEC61968.Assets.AssetInfo;

/**
 * Wire data that can be specified per line segment phase, or for the line segment
 * as a whole in case its phases all have the same wire characteristics.
 * @created 03-Jan-2024 11:56:23 AM
 */
public class WireInfo extends AssetInfo {

	/**
	 * (if there is a different core material) Radius of the central core.
	 */
	public Length coreRadius;
	/**
	 * (if used) Number of strands in the steel core.
	 */
	public Integer coreStrandCount;
	/**
	 * Geometric mean radius. If we replace the conductor by a thin walled tube of
	 * radius GMR, then its reactance is identical to the reactance of the actual
	 * conductor.
	 */
	public Length gmr;
	/**
	 * True if conductor is insulated.
	 */
	public Boolean insulated;
	/**
	 * (if insulated conductor) Material used for insulation.
	 */
	public WireInsulationKind insulationMaterial;
	/**
	 * (if insulated conductor) Thickness of the insulation.
	 */
	public Length insulationThickness;
	/**
	 * Conductor material.
	 */
	public WireMaterialKind material;
	/**
	 * AC resistance per unit length of the conductor at 25 øC.
	 */
	public ResistancePerLength rAC25;
	/**
	 * AC resistance per unit length of the conductor at 50 øC.
	 */
	public ResistancePerLength rAC50;
	/**
	 * AC resistance per unit length of the conductor at 75 øC.
	 */
	public ResistancePerLength rAC75;
	/**
	 * Outside radius of the wire.
	 */
	public Length radius;
	/**
	 * Current carrying capacity of the wire under stated thermal conditions.
	 */
	public CurrentFlow ratedCurrent;
	/**
	 * DC resistance per unit length of the conductor at 20 øC.
	 */
	public ResistancePerLength rDC20;
	/**
	 * Describes the wire gauge or cross section (e.g., 4/0, #2, 336.5).
	 */
	public String sizeDescription;
	/**
	 * Number of strands in the conductor.
	 */
	public Integer strandCount;
	public WirePhaseInfo WirePhaseInfo;

	public WireInfo(){

	}
}//end WireInfo