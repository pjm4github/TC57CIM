

import TC57CIM.IEC61970.Base.Domain.Susceptance;
import TC57CIM.IEC61970.Base.Domain.Length;
import TC57CIM.IEC61970.Base.Domain.Conductance;
import TC57CIM.IEC61970.Base.Domain.Resistance;
import TC57CIM.IEC61970.Base.Domain.Reactance;
import TC57CIM.IEC61970.Base.Core.Terminal;

/**
 * This class represents the zero sequence line mutual coupling.
 * @author pmora
 * @updated 15-Dec-2023 1:39:41 PM
 */
public class MutualCoupling {

	/**
	 * Zero sequence mutual coupling shunt (charging) susceptance, uniformly
	 * distributed, of the entire line section.
	 */
	private Susceptance b0ch;
	/**
	 * Distance to the start of the coupled region from the first line's terminal
	 * having sequence number equal to 1.
	 */
	private Length distance11;
	/**
	 * Distance to the end of the coupled region from the first line's terminal with
	 * sequence number equal to 1.
	 */
	private Length distance12;
	/**
	 * Distance to the start of coupled region from the second line's terminal with
	 * sequence number equal to 1.
	 */
	private Length distance21;
	/**
	 * Distance to the end of coupled region from the second line's terminal with
	 * sequence number equal to 1.
	 */
	private Length distance22;
	/**
	 * Zero sequence mutual coupling shunt (charging) conductance, uniformly
	 * distributed, of the entire line section.
	 */
	private Conductance g0ch;
	/**
	 * Zero sequence branch-to-branch mutual impedance coupling, resistance.
	 */
	private Resistance r0;
	/**
	 * Zero sequence branch-to-branch mutual impedance coupling, reactance.
	 */
	private Reactance x0;

	public MutualCoupling(){

	}

	public void finalize() throws Throwable {

	}

	public Susceptance getb0ch(){
		return b0ch;
	}

	public Length getdistance11(){
		return distance11;
	}

	public Length getdistance12(){
		return distance12;
	}

	public Length getdistance21(){
		return distance21;
	}

	public Length getdistance22(){
		return distance22;
	}

	public Terminal getFirst_Terminal(){
		return First_Terminal;
	}

	public Conductance getg0ch(){
		return g0ch;
	}

	public Resistance getr0(){
		return r0;
	}

	public Terminal getSecond_Terminal(){
		return Second_Terminal;
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
	public void setdistance11(Length newVal){
		distance11 = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setdistance12(Length newVal){
		distance12 = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setdistance21(Length newVal){
		distance21 = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setdistance22(Length newVal){
		distance22 = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setFirst_Terminal(Terminal newVal){
		First_Terminal = newVal;
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
	public void setr0(Resistance newVal){
		r0 = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setSecond_Terminal(Terminal newVal){
		Second_Terminal = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setx0(Reactance newVal){
		x0 = newVal;
	}

}