package IEC61968.AssetInfo;

import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.Voltage;
import IEC61968.Assets.AssetInfo;

/**
 * Busbar section data.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public class BusbarSectionInfo extends AssetInfo {

	/**
	 * Rated current.
	 */
	public CurrentFlow ratedCurrent;
	/**
	 * Rated voltage.
	 */
	public Voltage ratedVoltage;

	public BusbarSectionInfo(){

	}
}//end BusbarSectionInfo