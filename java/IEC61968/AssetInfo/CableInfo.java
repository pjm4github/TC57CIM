package IEC61968.AssetInfo;

import IEC61970.Base.Domain.Length;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Temperature;

/**
 * Cable data.
 * @created 03-Jan-2024 11:55:58 AM
 */
public class CableInfo extends WireInfo {

	/**
	 * Kind of construction of this cable.
	 */
	public CableConstructionKind constructionKind;
	/**
	 * Diameter over the core, including any semi-con screen; should be the insulating
	 * layer's inside diameter.
	 */
	public Length diameterOverCore;
	/**
	 * Diameter over the insulating layer, excluding outer screen.
	 */
	public Length diameterOverInsulation;
	/**
	 * Diameter over the outermost jacketing layer.
	 */
	public Length diameterOverJacket;
	/**
	 * Diameter over the outer screen; should be the shield's inside diameter.
	 */
	public Length diameterOverScreen;
	/**
	 * True if wire strands are extruded in a way to fill the voids in the cable.
	 */
	public Boolean isStrandFill;
	/**
	 * Maximum nominal design operating temperature.
	 */
	public Temperature nominalTemperature;
	/**
	 * Kind of outer jacket of this cable.
	 */
	public CableOuterJacketKind outerJacketKind;
	/**
	 * True if sheath / shield is used as a neutral (i.e., bonded).
	 */
	public Boolean sheathAsNeutral;
	/**
	 * Material of the shield.
	 */
	public CableShieldMaterialKind shieldMaterial;

	public CableInfo(){

	}
}//end CableInfo