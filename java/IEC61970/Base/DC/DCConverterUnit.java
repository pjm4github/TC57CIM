package IEC61970.Base.DC;


/**
 * Indivisible operative unit comprising all equipment between the point of common
 * coupling on the AC side and the point of common coupling - DC side, essentially
 * one or more converters, together with one or more converter transformers,
 * converter control equipment, essential protective and switching devices and
 * auxiliaries, if any, used for conversion.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public class DCConverterUnit extends DCEquipmentContainer {

	public DCConverterOperatingModeKind operationMode;

	public DCConverterUnit(){

	}
}//end DCConverterUnit