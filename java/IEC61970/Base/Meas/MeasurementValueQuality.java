package IEC61970.Base.Meas;

import IEC61970.InfIEC61970.SCADA_EMS.Meas.MeasurementValueQualityExt;

/**
 * Measurement quality flags. Bits 0-10 are defined for substation automation in
 * draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that
 * document. Bits 16-31 are reserved for EMS applications.
 * @created 02-Jan-2024 11:20:07 PM
 */
public class MeasurementValueQuality extends Quality61850 MeasurementValueQualityExt {

	public MeasurementValueQuality(){

	}
}//end MeasurementValueQuality