package IEC61968.DER;

import IEC61968.Metering.FlowDirectionKind;
import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Domain.Float;

/**
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class DERMonitorableParameter {

	public DERParameterKind DERParameter;
	public FlowDirectionKind flowDirection;
	public UnitMultiplier yMultiplier;
	public DERUnitSymbol yUnit;
	public Float yUnitInstalledMax;
	public Float yUnitInstalledMin;

	public DERMonitorableParameter(){

	}
}//end DERMonitorableParameter