

import TC57CIM.IEC61970.Base.Domain.String;

/**
 * A model of a set of individual Switches normally enclosed within the same
 * cabinet and possibly with interlocks that restrict the combination of switch
 * positions. These are typically found in medium voltage distribution networks.
 * A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted
 * switchgear, with primitive internal devices such as an internal bus-bar plus 3
 * or 4 internal switches each of which may individually be open or closed. A
 * CompositeSwitch and a set of contained Switches can also be used to represent a
 * multi-position switch e.g. a switch that can connect a circuit to Ground, Open
 * or Busbar.
 * @author pmora
 * @updated 15-Dec-2023 1:39:41 PM
 */
public class CompositeSwitch {

	/**
	 * An alphanumeric code that can be used as a reference to extra information such
	 * as the description of the interlocking scheme if any.
	 */
	private String compositeSwitchType;
	/**
	 * Switches contained in this Composite switch.
	 */
	private Switch Switches;

	public CompositeSwitch(){

	}

	public void finalize() throws Throwable {

	}

	public String getcompositeSwitchType(){
		return compositeSwitchType;
	}

	public Switch getSwitches(){
		return Switches;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setcompositeSwitchType(String newVal){
		compositeSwitchType = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setSwitches(Switch newVal){
		Switches = newVal;
	}

}