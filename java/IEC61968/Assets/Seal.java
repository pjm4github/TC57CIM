package IEC61968.Assets;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Physically controls access to AssetContainers.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class Seal extends IdentifiedObject {

	/**
	 * Date and time this seal has been applied.
	 */
	public DateTime appliedDateTime;
	/**
	 * Condition of seal.
	 */
	public SealConditionKind condition;
	/**
	 * Kind of seal.
	 */
	public SealKind kind;
	/**
	 * (reserved word) Seal number.
	 */
	public String sealNumber;

	public Seal(){

	}
}//end Seal