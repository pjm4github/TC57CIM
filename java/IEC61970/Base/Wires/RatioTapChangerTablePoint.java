package TC57CIM.IEC61970.Base.Wires;


/**
 * Describes each tap step in the ratio tap changer tabular curve.
 * @author SELAOST1
 * @version 1.0
 * @created 15-Dec-2023 4:38:29 PM
 */
public class RatioTapChangerTablePoint extends TapChangerTablePoint {

	/**
	 * Table of this point.
	 */
	public RatioTapChangerTable RatioTapChangerTable;

	public RatioTapChangerTablePoint(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}