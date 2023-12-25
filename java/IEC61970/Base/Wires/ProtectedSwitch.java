

import TC57CIM.IEC61970.Base.Domain.CurrentFlow;
import TC57CIM.IEC61970.Base.Protection.RecloseSequence;

/**
 * A ProtectedSwitch is a switching device that can be operated by
 * ProtectionEquipment.
 * @author pmora
 * @updated 15-Dec-2023 1:39:42 PM
 */
public class ProtectedSwitch extends Switch {

	/**
	 * The maximum fault current a breaking device can break safely under prescribed
	 * conditions of use.
	 */
	private CurrentFlow breakingCapacity;

	public ProtectedSwitch(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public CurrentFlow getbreakingCapacity(){
		return breakingCapacity;
	}

	public RecloseSequence getRecloseSequences(){
		return RecloseSequences;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setbreakingCapacity(CurrentFlow newVal){
		breakingCapacity = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setRecloseSequences(RecloseSequence newVal){
		RecloseSequences = newVal;
	}

}