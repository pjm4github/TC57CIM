package IEC61968.Metering;

import IEC61970.Base.Domain.Integer;

/**
 * Interharmonics are represented as a rational number 'numerator' / 'denominator',
 * and harmonics are represented using the same mechanism and identified by
 * 'denominator'=1.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class ReadingInterharmonic {

	/**
	 * Interharmonic denominator. Value 0 means not applicable. Value 2 is used in
	 * combination with 'numerator'=1 to represent interharmonic 1/2. Finally, value 1
	 * indicates the harmonic of the order specified with 'numerator'.
	 */
	public Integer denominator;
	/**
	 * Interharmonic numerator. Value 0 means not applicable. Value 1 is used in
	 * combination with 'denominator'=2 to represent interharmonic 1/2, and with
	 * 'denominator'=1 it represents fundamental frequency. Finally, values greater
	 * than 1 indicate the harmonic of that order (e.g., 'numerator'=5 is the fifth
	 * harmonic).
	 */
	public Integer numerator;

	public ReadingInterharmonic(){

	}
}//end ReadingInterharmonic