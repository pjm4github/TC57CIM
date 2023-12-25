

import TC57CIM.IEC61970.Base.Domain.Susceptance;
import TC57CIM.IEC61970.Base.Domain.Conductance;
import TC57CIM.IEC61970.Base.Domain.Resistance;
import TC57CIM.IEC61970.Base.Domain.Temperature;
import TC57CIM.IEC61970.Base.Domain.Reactance;

/**
 * A wire or combination of wires, with consistent electrical characteristics,
 * building a single electrical system, used to carry alternating current between
 * points in the power system.
 * For symmetrical, transposed 3ph lines, it is sufficient to use  attributes of
 * the line segment, which describe impedances and admittances for the entire
 * length of the segment.  Additionally impedances can be computed by using length
 * and associated per length impedances.
 * The BaseVoltage at the two ends of ACLineSegments in a Line shall have the same
 * BaseVoltage.nominalVoltage. However, boundary lines  may have slightly
 * different BaseVoltage.nominalVoltages and  variation is allowed. Larger voltage
 * difference in general requires use of an equivalent branch.
 * @author pmora
 * @updated 15-Dec-2023 1:39:41 PM
 */
public class ACLineSegment extends Conductor {

	/**
	 * Zero sequence shunt (charging) susceptance, uniformly distributed, of the
	 * entire line section.
	 */
	private Susceptance b0ch;
	/**
	 * Positive sequence shunt (charging) susceptance, uniformly distributed, of the
	 * entire line section.  This value represents the full charging over the full
	 * length of the line.
	 */
	private Susceptance bch;
	/**
	 * Zero sequence shunt (charging) conductance, uniformly distributed, of the
	 * entire line section.
	 */
	private Conductance g0ch;
	/**
	 * Positive sequence shunt (charging) conductance, uniformly distributed, of the
	 * entire line section.
	 */
	private Conductance gch;
	/**
	 * Positive sequence series resistance of the entire line section.
	 */
	private Resistance r;
	/**
	 * Zero sequence series resistance of the entire line section.
	 */
	private Resistance r0;
	/**
	 * Maximum permitted temperature at the end of SC for the calculation of minimum
	 * short-circuit currents. Used for short circuit data exchange according to IEC
	 * 60909
	 */
	private Temperature shortCircuitEndTemperature;
	/**
	 * Positive sequence series reactance of the entire line section.
	 */
	private Reactance x;
	/**
	 * Zero sequence series reactance of the entire line section.
	 */
	private Reactance x0;
	/**
	 * The clamps connected to the line segment.
	 */
	private Clamp Clamp;

	public ACLineSegment(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public Susceptance getb0ch(){
		return b0ch;
	}

	public Susceptance getbch(){
		return bch;
	}

	public Clamp getClamp(){
		return Clamp;
	}

	public Conductance getg0ch(){
		return g0ch;
	}

	public Conductance getgch(){
		return gch;
	}

	public Resistance getr(){
		return r;
	}

	public Resistance getr0(){
		return r0;
	}

	public Temperature getshortCircuitEndTemperature(){
		return shortCircuitEndTemperature;
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
	public void setb0ch(Susceptance newVal){
		b0ch = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setbch(Susceptance newVal){
		bch = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setClamp(Clamp newVal){
		Clamp = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setg0ch(Conductance newVal){
		g0ch = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setgch(Conductance newVal){
		gch = newVal;
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
	public void setshortCircuitEndTemperature(Temperature newVal){
		shortCircuitEndTemperature = newVal;
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