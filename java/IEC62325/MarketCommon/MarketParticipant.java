package IEC62325.MarketCommon;

import IEC62325.MarketOperations.ReferenceData.MarketPerson;
import IEC61968.Common.Organisation;
import IEC62325.MarketManagement.MarketDocument;

/**
 * An identification of a party acting in a electricity market business process.
 * This class is used to identify organizations that can participate in market
 * management and/or market operations.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class MarketParticipant extends Organisation {

	public MarketPerson MarketPerson;
	public MarketDocument MarketDocument;

	public MarketParticipant(){

	}
}//end MarketParticipant