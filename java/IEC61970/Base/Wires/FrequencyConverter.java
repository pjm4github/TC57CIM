

import TC57CIM.IEC61970.Base.Domain.Frequency;
import TC57CIM.IEC61970.Base.Domain.ActivePower;
import TC57CIM.IEC61970.Base.Domain.Voltage;

/**
 * A device to convert from one frequency to another (e.g., frequency F1 to F2)
 * comprises a pair of FrequencyConverter instances. One converts from F1 to DC,
 * the other converts the DC to F2.
 * @author pmora
 * @updated 15-Dec-2023 1:39:41 PM
 */
public class FrequencyConverter extends RegulatingCondEq {

	/**
	 * Frequency on the AC side.
	 */
	private Frequency frequency;
	/**
	 * The maximum active power on the DC side at which the frequence converter should
	 * operate.
	 */
	private ActivePower maxP;
	/**
	 * The maximum voltage on the DC side at which the frequency converter should
	 * operate.
	 */
	private Voltage maxU;
	/**
	 * The minimum active power on the DC side at which the frequence converter should
	 * operate.
	 */
	private ActivePower minP;
	/**
	 * The minimum voltage on the DC side at which the frequency converter should
	 * operate.
	 */
	private Voltage minU;

	public FrequencyConverter(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public Frequency getfrequency(){
		return frequency;
	}

	public ActivePower getmaxP(){
		return maxP;
	}

	public Voltage getmaxU(){
		return maxU;
	}

	public ActivePower getminP(){
		return minP;
	}

	public Voltage getminU(){
		return minU;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setfrequency(Frequency newVal){
		frequency = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setmaxP(ActivePower newVal){
		maxP = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setmaxU(Voltage newVal){
		maxU = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setminP(ActivePower newVal){
		minP = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setminU(Voltage newVal){
		minU = newVal;
	}

}