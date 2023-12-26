package IEC61968.AssetInfo;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.Length;

/**
 * Tape shield cable data.
 * @author Tom
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class TapeShieldCableInfo extends CableInfo {

	/**
	 * Percentage of the tape shield width that overlaps in each wrap, typically 10%
	 * to 25%.
	 */
	public PerCent tapeLap;
	/**
	 * Thickness of the tape shield, before wrapping.
	 */
	public Length tapeThickness;

	public TapeShieldCableInfo(){

	}
}//end TapeShieldCableInfo