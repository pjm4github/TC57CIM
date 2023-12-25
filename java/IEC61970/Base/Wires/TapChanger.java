

import TC57CIM.IEC61970.Base.Domain.Seconds;
import TC57CIM.IEC61970.Base.Domain.Voltage;

/**
 * Mechanism for changing transformer winding tap positions.
 * @author pmora
 * @updated 15-Dec-2023 1:39:42 PM
 */
public class TapChanger {

	/**
	 * Specifies the regulation status of the equipment.  True is regulating, false is
	 * not regulating.
	 */
	private boolean controlEnabled;
	/**
	 * Highest possible tap step position, advance from neutral.
	 * The attribute shall be greater than lowStep.
	 */
	private int highStep;
	/**
	 * For an LTC, the delay for initial tap changer operation (first step change)
	 */
	private Seconds initialDelay;
	/**
	 * Lowest possible tap step position, retard from neutral
	 */
	private int lowStep;
	/**
	 * Specifies whether or not a TapChanger has load tap changing capabilities.
	 */
	private boolean ltcFlag;
	/**
	 * The neutral tap step position for this winding.
	 * The attribute shall be equal or greater than lowStep and equal or less than
	 * highStep.
	 */
	private int neutralStep;
	/**
	 * Voltage at which the winding operates at the neutral tap setting.
	 */
	private Voltage neutralU;
	/**
	 * The tap step position used in "normal" network operation for this winding. For
	 * a "Fixed" tap changer indicates the current physical tap setting.
	 * The attribute shall be equal or greater than lowStep and equal or less than
	 * highStep.
	 */
	private int normalStep;
	/**
	 * Tap changer position.
	 * Starting step for a steady state solution. Non integer values are allowed to
	 * support continuous tap variables. The reasons for continuous value are to
	 * support study cases where no discrete tap changers has yet been designed, a
	 * solutions where a narrow voltage band force the tap step to oscillate or
	 * accommodate for a continuous solution as input.
	 * The attribute shall be equal or greater than lowStep and equal or less than
	 * highStep.
	 */
	private float step;
	/**
	 * For an LTC, the delay for subsequent tap changer operation (second and later
	 * step changes)
	 */
	private Seconds subsequentDelay;
	/**
	 * The regulating control scheme in which this tap changer participates.
	 */
	private TapChangerControl TapChangerControl;

	public TapChanger(){

	}

	public void finalize() throws Throwable {

	}

	public boolean getcontrolEnabled(){
		return controlEnabled;
	}

	public int gethighStep(){
		return highStep;
	}

	public Seconds getinitialDelay(){
		return initialDelay;
	}

	public int getlowStep(){
		return lowStep;
	}

	public boolean getltcFlag(){
		return ltcFlag;
	}

	public int getneutralStep(){
		return neutralStep;
	}

	public Voltage getneutralU(){
		return neutralU;
	}

	public int getnormalStep(){
		return normalStep;
	}

	public float getstep(){
		return step;
	}

	public Seconds getsubsequentDelay(){
		return subsequentDelay;
	}

	public TapChangerControl getTapChangerControl(){
		return TapChangerControl;
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
	public void sethighStep(int newVal){
		highStep = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setinitialDelay(Seconds newVal){
		initialDelay = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setlowStep(int newVal){
		lowStep = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setltcFlag(boolean newVal){
		ltcFlag = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setneutralStep(int newVal){
		neutralStep = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setneutralU(Voltage newVal){
		neutralU = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setnormalStep(int newVal){
		normalStep = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setstep(float newVal){
		step = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setsubsequentDelay(Seconds newVal){
		subsequentDelay = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setTapChangerControl(TapChangerControl newVal){
		TapChangerControl = newVal;
	}

}