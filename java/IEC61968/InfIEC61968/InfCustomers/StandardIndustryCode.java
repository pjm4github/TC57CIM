package IEC61968.InfIEC61968.InfCustomers;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Document;

/**
 * The Standard Industrial Classification (SIC) are the codes that identify the
 * type of products/service an industry is involved in, and used for statutory
 * reporting purposes. For example, in the USA these codes are located by the
 * federal government, and then published in a book entitled "The Standard
 * Industrial Classification Manual". The codes are arranged in a hierarchical
 * structure.
 * Note that Residential Service Agreements are not classified according to the
 * SIC codes.
 * @created 29-Dec-2023 9:26:01 PM
 */
public class StandardIndustryCode extends Document {

	/**
	 * Standard alphanumeric code assigned to a particular product/service within an
	 * industry.
	 */
	public String code;

	public StandardIndustryCode(){

	}
}//end StandardIndustryCode