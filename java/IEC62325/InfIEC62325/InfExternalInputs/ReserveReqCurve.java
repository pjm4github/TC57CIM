package IEC62325.InfIEC62325.InfExternalInputs;

import IEC61970.Base.Core.Curve;

/**
 * A curve relating  reserve requirement versus time, showing the values of a
 * specific reserve requirement for each unit of the period covered. The  curve
 * can be based on "absolute" time or on "normalized' time.
 * X is time, typically expressed in absolute time
 * Y1 is reserve requirement, typically expressed in MW
 * @created 03-Jan-2024 1:51:06 PM
 */
public class ReserveReqCurve extends Curve {

	public ReserveReq ReserveReq;

	public ReserveReqCurve(){

	}
}//end ReserveReqCurve