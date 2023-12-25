

import TC57CIM.IEC61970.Base.Domain.CurrentFlow;
import TC57CIM.IEC61970.Base.Domain.DateTime;

/**
 * A generic device designed to close, or open, or both, one or more electric
 * circuits.  All switches are two terminal devices including grounding switches.
 * @author pmora
 * @updated 15-Dec-2023 1:39:42 PM
 */
public class Switch {

	/**
	 * The attribute is used in cases when no Measurement for the status value is
	 * present. If the Switch has a status measurement the Discrete.normalValue is
	 * expected to match with the Switch.normalOpen.
	 */
	private boolean normalOpen;
	/**
	 * The attribute tells if the switch is considered open when used as input to
	 * topology processing.
	 */
	private boolean open;
	/**
	 * The maximum continuous current carrying capacity in amps governed by the device
	 * material and construction.
	 */
	private CurrentFlow ratedCurrent;
	/**
	 * Branch is retained in a bus branch model.  The flow through retained switches
	 * will normally be calculated in power flow.
	 */
	private boolean retained;
	/**
	 * The switch on count since the switch was last reset or initialized.
	 */
	private int switchOnCount;
	/**
	 * The date and time when the switch was last switched on.
	 */
	private DateTime switchOnDate;
	/**
	 * The individual switch phases for the switch.
	 */
	private SwitchPhase SwitchPhase;
	/**
	 * A Switch can be associated with SwitchSchedules.
	 */
	private SwitchSchedule SwitchSchedules;

	public Switch(){

	}

	public void finalize() throws Throwable {

	}

	public boolean getnormalOpen(){
		return normalOpen;
	}

	public boolean getopen(){
		return open;
	}

	public CurrentFlow getratedCurrent(){
		return ratedCurrent;
	}

	public boolean getretained(){
		return retained;
	}

	public int getswitchOnCount(){
		return switchOnCount;
	}

	public DateTime getswitchOnDate(){
		return switchOnDate;
	}

	public SwitchPhase getSwitchPhase(){
		return SwitchPhase;
	}

	public SwitchSchedule getSwitchSchedules(){
		return SwitchSchedules;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setnormalOpen(boolean newVal){
		normalOpen = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setopen(boolean newVal){
		open = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setratedCurrent(CurrentFlow newVal){
		ratedCurrent = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setretained(boolean newVal){
		retained = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setswitchOnCount(int newVal){
		switchOnCount = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setswitchOnDate(DateTime newVal){
		switchOnDate = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setSwitchPhase(SwitchPhase newVal){
		SwitchPhase = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setSwitchSchedules(SwitchSchedule newVal){
		SwitchSchedules = newVal;
	}

}