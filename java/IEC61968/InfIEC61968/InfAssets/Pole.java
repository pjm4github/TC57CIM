package IEC61968.InfIEC61968.InfAssets;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Length;
import IEC61970.Base.Domain.DateTime;
import IEC61968.Assets.Structure;
import IEC61968.Assets.Streetlight;

/**
 * Pole asset.
 * @created 03-Jan-2024 12:26:35 PM
 */
public class Pole extends Structure {

	/**
	 * Kind of base for this pole.
	 */
	public PoleBaseKind baseKind;
	/**
	 * True if a block of material has been attached to base of pole in ground for
	 * stability. This technique is used primarily when anchors can not be used.
	 */
	public Boolean breastBlock;
	/**
	 * Pole class: 1, 2, 3, 4, 5, 6, 7, H1, H2, Other, Unknown.
	 */
	public String classification;
	/**
	 * The framing structure mounted on the pole.
	 */
	public String construction;
	/**
	 * Diameter of the pole.
	 */
	public Length diameter;
	/**
	 * Joint pole agreement reference number.
	 */
	public String jpaReference;
	/**
	 * Length of the pole (inclusive of any section of the pole that may be
	 * underground post-installation).
	 */
	public Length length;
	/**
	 * Kind of preservative for this pole.
	 */
	public PolePreservativeKind preservativeKind;
	/**
	 * Pole species. Aluminum, Aluminum Davit, Concrete, Fiberglass, Galvanized Davit,
	 * Galvanized, Steel Davit Primed, Steel Davit, Steel Standard Primed, Steel,
	 * Truncated, Wood-Treated, Wood-Hard, Wood-Salt Treated, Wood-Soft, Wood, Other,
	 * Unknown.
	 */
	public String speciesType;
	/**
	 * Date and time pole was last treated with preservative.
	 */
	public DateTime treatedDateTime;
	/**
	 * Kind of treatment for this pole.
	 */
	public PoleTreatmentKind treatmentKind;
	/**
	 * All streetlights attached to this pole.
	 */
	public Streetlight Streetlights;

	public Pole(){

	}
}//end Pole