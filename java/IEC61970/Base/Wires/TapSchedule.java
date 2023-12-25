


/**
 * A pre-established pattern over time for a tap step.
 * @author pmora
 * @updated 15-Dec-2023 1:39:42 PM
 */
public class TapSchedule {

	/**
	 * A TapSchedule is associated with a TapChanger.
	 */
	private TapChanger TapChanger;

	public TapSchedule(){

	}

	public void finalize() throws Throwable {

	}

	public TapChanger getTapChanger(){
		return TapChanger;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setTapChanger(TapChanger newVal){
		TapChanger = newVal;
	}

}