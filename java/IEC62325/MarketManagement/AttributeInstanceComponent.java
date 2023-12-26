package IEC62325.MarketManagement;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;

/**
 * A class used to provide information about an attribute.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class AttributeInstanceComponent {

	/**
	 * The identification of the formal name of an attribute.
	 */
	public String attribute;
	/**
	 * The instance value of the attribute.
	 */
	public String attributeValue;
	/**
	 * A sequential value representing a relative sequence number.
	 */
	public Integer position;
	public TimeSeries TimeSeries;

	public AttributeInstanceComponent(){

	}
}//end AttributeInstanceComponent