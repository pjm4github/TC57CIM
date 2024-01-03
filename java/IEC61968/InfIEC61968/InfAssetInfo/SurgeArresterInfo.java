package IEC61968.InfIEC61968.InfAssetInfo;

import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61968.Assets.AssetInfo;

/**
 * Properties of surge arrester.
 * @created 29-Dec-2023 6:23:27 PM
 */
public class SurgeArresterInfo extends AssetInfo {

	/**
	 * Maximum continuous power frequency voltage allowed on the surge arrester.
	 */
	public Voltage continuousOperatingVoltage;
	/**
	 * If true, the arrester has a polymer housing, porcelain otherwise.
	 */
	public Boolean isPolymer;
	/**
	 * Residual voltage during an 8x20 microsecond current impulse at the nominal
	 * discharge current level.
	 */
	public Voltage lightningImpulseDischargeVoltage;
	/**
	 * Determines the arrester energy discharge capability.  Choices are limited to 0
	 * (none) through 5 (highest) by IEC 60099. Classes 1..3 require a 10-kA nominal
	 * discharge current. Classes 4..5 require a 20-kA nominal discharge current.
	 * Lower nominal discharge currents must use class 0.
	 */
	public Integer lineDischargeClass;
	/**
	 * The lightning discharge current used to classify the arrester. Choices are
	 * limited to 1.5, 2.5, 5, 10, and 20 kA by IEC 60099.
	 */
	public CurrentFlow nominalDischargeCurrent;
	/**
	 * Fault current level at which all parts of the failed arrester lie within a
	 * circle prescribed by IEC 60099.
	 */
	public CurrentFlow pressureReliefClass;
	/**
	 * The temporary overvoltage (TOV) level at power frequency that the surge
	 * arrester withstands for 10 seconds.
	 */
	public Voltage ratedVoltage;
	/**
	 * Residual voltage during a current impulse with front time of 1 microsecond, and
	 * magnitude equal to the nominal discharge current level.
	 */
	public Voltage steepFrontDischargeVoltage;
	/**
	 * Residual voltage during a current impulse with front time of at least 30
	 * microseconds, and magnitude specified in IEC 60099 for the line discharge class.
	 * Does not apply to line discharge class 0.
	 */
	public Voltage switchingImpulseDischargeVoltage;

	public SurgeArresterInfo(){

	}
}//end SurgeArresterInfo