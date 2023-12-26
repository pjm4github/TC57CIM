package IEC61968.DER;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.DateTime;

/**
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class DERCurveData {

	public Integer intervalNumber;
	public Float maxYValue;
	public Float minYValue;
	public Float nominalYValue;
	public DateTime timeStamp;
	public DispatchSchedule DispatchSchedule;
	public DERMonitorableParameter DERMonitorableParameter;

	public DERCurveData(){

	}
}//end DERCurveData