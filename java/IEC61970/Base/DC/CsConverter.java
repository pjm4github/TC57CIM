package TC57CIM.IEC61970.Base.DC;

import TC57CIM.IEC61970.Base.Domain.AngleDegrees;
import TC57CIM.IEC61970.Base.Domain.CurrentFlow;

/**
 * DC side of the current source converter (CSC).
 * @author T. Kostic
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class CsConverter extends ACDCConverter {

	/**
	 * Firing angle, typical value between 10 and 18 degrees for a rectifier. CSC
	 * state variable, result from power flow.
	 */
	public AngleDegrees alpha;
	/**
	 * Extinction angle. CSC state variable, result from power flow.
	 */
	public AngleDegrees gamma;
	/**
	 * Maximum firing angle. CSC configuration data used in power flow.
	 */
	public AngleDegrees maxAlpha;
	/**
	 * Maximum extinction angle. CSC configuration data used in power flow.
	 */
	public AngleDegrees maxGamma;
	/**
	 * The maximum direct current (Id) on the DC side at which the converter should
	 * operate. Converter configuration data use in power flow.
	 */
	public CurrentFlow maxIdc;
	/**
	 * Minimum firing angle. CSC configuration data used in power flow.
	 */
	public AngleDegrees minAlpha;
	/**
	 * Minimum extinction angle. CSC configuration data used in power flow.
	 */
	public AngleDegrees minGamma;
	/**
	 * The minimum direct current (Id) on the DC side at which the converter should
	 * operate. CSC configuration data used in power flow.
	 */
	public CurrentFlow minIdc;
	/**
	 * Indicates whether the DC pole is operating as an inverter or as a rectifier.
	 * CSC control variable used in power flow.
	 */
	public CsOperatingModeKind operatingMode;
	public CsPpccControlKind pPccControl;
	/**
	 * Rated converter DC current, also called IdN. Converter configuration data used
	 * in power flow.
	 */
	public CurrentFlow ratedIdc;
	/**
	 * Target firing angle. CSC control variable used in power flow.
	 */
	public AngleDegrees targetAlpha;
	/**
	 * Target extinction angle. CSC  control variable used in power flow.
	 */
	public AngleDegrees targetGamma;
	/**
	 * DC current target value. CSC control variable used in power flow.
	 */
	public CurrentFlow targetIdc;

	public CsConverter(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}