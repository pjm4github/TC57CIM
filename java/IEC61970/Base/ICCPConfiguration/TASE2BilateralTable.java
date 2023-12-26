package IEC61970.Base.ICCPConfiguration;

import IEC61970.Base.Domain.String;

/**
 * This class describe the sending (providing) side in a bilateral ICCP data
 * exchange. Hence the ICCP bilateral (table) descriptions are created by
 * exchanging ICCP Provider data between the parties.
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class TASE2BilateralTable extends BilateralExchangeAgreement {

	/**
	 * Specifies the version of the Bilateral Table configuration that is being
	 * exchanged.
	 */
	public String bilateralTableID;
	/**
	 * The Version attribute identifies a unique version of the Bilateral Table. If
	 * any changes are made to a Bilateral Table, then a new unique value for this
	 * attribute shall be generated.
	 */
	public String bilateralTableVersion;
	/**
	 * Specifies the version of the TASE.2 that is needed to access the Bilateral
	 * Table information via TASE.2.
	 * 
	 * In order for a link to be established, both sides must have the same value.
	 */
	public String tase2version;

	public TASE2BilateralTable(){

	}
}//end TASE2BilateralTable