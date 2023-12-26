package IEC61968.Metering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Detailed description for a quality of a reading value, produced by an end
 * device or a system. Values in attributes allow for creation of the recommended
 * codes to be used for identifying reading value quality codes as follows:
 * <systemId>.<category>.<subCategory>.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class ReadingQualityType extends IdentifiedObject {

	/**
	 * High-level nature of the reading value quality.
	 */
	public String category;
	/**
	 * More specific nature of the reading value quality, as a further sub-
	 * categorisation of 'category'.
	 */
	public String subCategory;
	/**
	 * Identification of the system which has declared the issue with the data or
	 * provided commentary on the data.
	 */
	public String systemId;

	public ReadingQualityType(){

	}
}//end ReadingQualityType