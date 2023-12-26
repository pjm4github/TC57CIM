package IEC61968.DER;

import IEC61970.Base.Domain.Boolean;
import IEC61968.Metering.EndDeviceGroup;

/**
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class DERFunction {

	public Boolean connectDisconnect;
	public Boolean frequencyWattCurveFunction;
	public Boolean maxRealPowerLimiting;
	public Boolean rampRateControl;
	public Boolean reactivePowerDispatch;
	public Boolean realPowerDispatch;
	public Boolean voltageRegulation;
	public Boolean voltVarCurveFunction;
	public Boolean voltWattCurveFunction;
	public EndDeviceGroup EndDeviceGroup;

	public DERFunction(){

	}
}//end DERFunction