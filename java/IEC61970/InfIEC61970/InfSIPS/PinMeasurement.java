package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Meas.Measurement;

/**
 * Gate input pin that is associated with a Measurement or a calculation of
 * Measurement.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:32:50 PM
 */
public class PinMeasurement extends GateInputPin {

	public Measurement Measurement;

	public PinMeasurement(){

	}
}//end PinMeasurement