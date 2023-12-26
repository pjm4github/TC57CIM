package IEC61968.Metering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;

/**
 * Quality of a specific reading value or interval reading value. Note that more
 * than one quality may be applicable to a given reading. Typically not used
 * unless problems or unusual conditions occur (i.e., quality for each reading is
 * assumed to be good unless stated otherwise in associated reading quality type).
 * It can also be used with the corresponding reading quality type to indicate
 * that the validation has been performed and succeeded.
 * @created 25-Dec-2023 8:45:24 PM
 */
public class ReadingQuality {

	/**
	 * Elaboration on the quality code.
	 */
	public String comment;
	/**
	 * System acting as the source of the quality code.
	 */
	public String source;
	/**
	 * Date and time at which the quality code was assigned or ascertained.
	 */
	public DateTime timeStamp;
	/**
	 * Reading value to which this quality applies.
	 */
	public BaseReading Reading;
	/**
	 * Type of this reading quality.
	 */
	public ReadingQualityType ReadingQualityType;

	public ReadingQuality(){

	}
}//end ReadingQuality