

import TC57CIM.IEC61970.Base.Domain.Resistance;
import TC57CIM.IEC61970.Base.Domain.CurrentFlow;
import TC57CIM.IEC61970.Base.Domain.Voltage;
import TC57CIM.IEC61970.Base.Domain.Reactance;

/**
 * A Series Compensator is a series capacitor or reactor or an AC transmission
 * line without charging susceptance.  It is a two terminal device.
 * @author pmora
 * @updated 15-Dec-2023 1:39:42 PM
 */
public class SeriesCompensator {

	/**
	 * Positive sequence resistance.
	 */
	private Resistance r;
	/**
	 * Zero sequence resistance.
	 */
	private Resistance r0;
	/**
	 * Describe if a metal oxide varistor (mov) for over voltage protection is
	 * configured at the series compensator.
	 */
	private boolean varistorPresent;
	/**
	 * The maximum current the varistor is designed to handle at specified duration.
	 */
	private CurrentFlow varistorRatedCurrent;
	/**
	 * The dc voltage at which the varistor start conducting.
	 */
	private Voltage varistorVoltageThreshold;
	/**
	 * Positive sequence reactance.
	 */
	private Reactance x;
	/**
	 * Zero sequence reactance.
	 */
	private Reactance x0;

	public SeriesCompensator(){

	}

	public void finalize() throws Throwable {

	}

	public Resistance getr(){
		return r;
	}

	public Resistance getr0(){
		return r0;
	}

	public boolean getvaristorPresent(){
		return varistorPresent;
	}

	public CurrentFlow getvaristorRatedCurrent(){
		return varistorRatedCurrent;
	}

	public Voltage getvaristorVoltageThreshold(){
		return varistorVoltageThreshold;
	}

	public Reactance getx(){
		return x;
	}

	public Reactance getx0(){
		return x0;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setr(Resistance newVal){
		r = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setr0(Resistance newVal){
		r0 = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setvaristorPresent(boolean newVal){
		varistorPresent = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setvaristorRatedCurrent(CurrentFlow newVal){
		varistorRatedCurrent = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setvaristorVoltageThreshold(Voltage newVal){
		varistorVoltageThreshold = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setx(Reactance newVal){
		x = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setx0(Reactance newVal){
		x0 = newVal;
	}

}