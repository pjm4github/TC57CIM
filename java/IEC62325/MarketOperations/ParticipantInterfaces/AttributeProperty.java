package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.MarketOpCommon.MktUserAttribute;

/**
 * Property for a particular attribute that contains name and value.
 * @created 28-Dec-2023 5:18:13 PM
 */
public class AttributeProperty {

	public String propertyName;
	public String propertyValue;
	public String sequence;
	public MktUserAttribute MktUserAttribute;

	public AttributeProperty(){

	}
}//end AttributeProperty