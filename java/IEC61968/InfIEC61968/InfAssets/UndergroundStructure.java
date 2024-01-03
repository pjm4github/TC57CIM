package IEC61968.InfIEC61968.InfAssets;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Date;
import IEC61968.Assets.Structure;

/**
 * Underground structure.
 * @created 29-Dec-2023 6:12:28 PM
 */
public class UndergroundStructure extends Structure {

	/**
	 * True if vault is ventilating.
	 */
	public Boolean hasVentilation;
	/**
	 * True if vault is ventilating.
	 */
	public UndergroundStructureKind kind;
	/**
	 * Primary material of underground structure.
	 */
	public String material;
	/**
	 * Date sealing warranty expires.
	 */
	public Date sealingWarrantyExpiresDate;

	public UndergroundStructure(){

	}
}//end UndergroundStructure