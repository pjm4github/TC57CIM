

import TC57CIM.IEC61970.Base.Domain.Length;

/**
 * Combination of conducting material with consistent electrical characteristics,
 * building a single electrical system, used to carry current between points in
 * the power system.
 * @author pmora
 * @updated 15-Dec-2023 1:39:41 PM
 */
public class Conductor {

	/**
	 * Segment length for calculating line section capabilities
	 */
	private Length length;

	public Conductor(){

	}

	public void finalize() throws Throwable {

	}

	public Length getlength(){
		return length;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setlength(Length newVal){
		length = newVal;
	}

}