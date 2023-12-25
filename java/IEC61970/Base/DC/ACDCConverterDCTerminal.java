package TC57CIM.IEC61970.Base.DC;


/**
 * A DC electrical connection point at the AC/DC converter. The AC/DC converter is
 * electrically connected also to the AC side. The AC connection is inherited from
 * the AC conducting equipment in the same way as any other AC equipment. The
 * AC/DC converter DC terminal is separate from generic DC terminal to restrict
 * the connection with the AC side to AC/DC converter and so that no other DC
 * conducting equipment can be connected to the AC side.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class ACDCConverterDCTerminal extends DCBaseTerminal {

	/**
	 * Represents the normal network polarity condition.
	 */
	public DCPolarityKind polarity;
	/**
	 * A DC converter terminal belong to an DC converter.
	 */
	public ACDCConverter DCConductingEquipment;

	public ACDCConverterDCTerminal(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}