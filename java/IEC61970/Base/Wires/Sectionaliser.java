package IEC61970.Base.Wires;


/**
 * Automatic switch that will lock open to isolate a faulted section. It may, or
 * may not, have load breaking capability. Its primary purpose is to provide fault
 * sectionalising at locations where the fault current is either too high, or too
 * low, for proper coordination of fuses.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class Sectionaliser extends Switch {

	public Sectionaliser(){

	}
}//end Sectionaliser