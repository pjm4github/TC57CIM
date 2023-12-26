package IEC61970.Part303.GenericDataset;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Date;

/**
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GenericDataSetVersion {

	/**
	 * The universal CIM version name describing a consistent set of packages. 
	 */
	public String majorVersion = 2016;
	/**
	 * Describe minor updates and error corrections.
	 */
	public String minorVersion = 01;
	/**
	 * The date when the complete CIM canonical model is published and made available
	 * for use,
	 * After the publication the major version and name space are updated.
	 */
	public Date published;

	public GenericDataSetVersion(){

	}
}//end GenericDataSetVersion