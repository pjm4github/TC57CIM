package IEC61968.AssetMeas;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Temperature;
import IEC61970.Base.Meas.Analog;
import IEC61968.Assets.TestStandard;

/**
 * Definition of type of analog useful in asset domain.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public class AssetAnalog extends Analog {

	/**
	 * Detection limit of related analog value if different from detection limit of
	 * test standard or if there is no test standard. The detection limit (also known
	 * as lower limit of detection or limit of detection (LOD), is the lowest quantity
	 * of a substance that can be distinguished from the absence of that substance (a
	 * blank value) within a stated confidence limit (generally 1%).
	 */
	public Float detectionLimit;
	/**
	 * Precision of related analog value if different from precision of test standard
	 * or if there is no test standard. Precision is a measure of how closely
	 * individual measurements agree with one another. Expressed as 'plus or minus'
	 * the value of this attribute.
	 */
	public Float precision;
	/**
	 * Reporting temperature of related analog value if different from reporting
	 * temperature of test standard or if there is no test standard. Reporting
	 * temperature is what gas volumes are normalized to. Different reporting
	 * temperatures are used by different sources. For example, ASTM specifies 0øC,
	 * whereas IEC specifies 20øC. Online monitors often have their own unique
	 * reporting temperatures. 
	 */
	public Temperature reportingTemperature;
	/**
	 * The lab test standard to which this asset health analog is related.
	 */
	public TestStandard TestStandard;

	public AssetAnalog(){

	}
}//end AssetAnalog