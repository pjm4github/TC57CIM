package TC57CIM.IEC61970.Base.DC;


/**
 * Indivisible operative unit comprising all equipment between the point of common
 * coupling on the AC side and the point of common coupling  DC side, essentially
 * one or more converters, together with one or more converter transformers,
 * converter control equipment, essential protective and switching devices and
 * auxiliaries, if any, used for conversion.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class DCConverterUnit extends DCEquipmentContainer {

	public DCConverterOperatingModeKind operationMode;

	public DCConverterUnit(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}