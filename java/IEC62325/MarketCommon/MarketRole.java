package IEC62325.MarketCommon;

import IEC61970.Base.Domain.String;
import IEC61968.Common.OrganisationRole;

/**
 * The external intended behavior played by a party within the electricity market.
 * @created 03-Jan-2024 1:56:04 PM
 */
public class MarketRole extends OrganisationRole {

	/**
	 * The kind of market roles that can be played by parties for given domains within
	 * the electricity market. Types are flexible using dataType of string for free-
	 * entry of role types.
	 */
	public String type;
	public MarketParticipant MarketParticipant;

	public MarketRole(){

	}
}//end MarketRole