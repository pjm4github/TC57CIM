


/**
 * A type of conducting equipment that can regulate a quantity (i.e. voltage or
 * flow) at a specific point in the network.
 * @author pmora
 * @updated 15-Dec-2023 1:39:42 PM
 */
public class RegulatingCondEq extends EnergyConnection {

	/**
	 * Specifies the regulation status of the equipment.  True is regulating, false is
	 * not regulating.
	 */
	private boolean controlEnabled;
	/**
	 * The regulating control scheme in which this equipment participates.
	 */
	private RegulatingControl RegulatingControl;

	public RegulatingCondEq(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public boolean getcontrolEnabled(){
		return controlEnabled;
	}

	public RegulatingControl getRegulatingControl(){
		return RegulatingControl;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setcontrolEnabled(boolean newVal){
		controlEnabled = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setRegulatingControl(RegulatingControl newVal){
		RegulatingControl = newVal;
	}

}