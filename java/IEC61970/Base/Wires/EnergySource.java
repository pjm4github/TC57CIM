

import TC57CIM.IEC61970.Base.Domain.ActivePower;
import TC57CIM.IEC61970.Base.Domain.Voltage;
import TC57CIM.IEC61970.Base.Domain.Resistance;
import TC57CIM.IEC61970.Base.Domain.ReactivePower;
import TC57CIM.IEC61970.Base.Domain.AngleRadians;
import TC57CIM.IEC61970.Base.Domain.Reactance;
import TC57CIM.IEC61970.InfIEC61970.InfEnergySource.EnergySchedulingType;

/**
 * A generic equivalent for an energy supplier on a transmission or distribution
 * voltage level.
 * @author pmora
 * @updated 15-Dec-2023 1:39:41 PM
 */
public class EnergySource extends EnergyConnection {

	/**
	 * High voltage source active injection. Load sign convention is used, i.e.
	 * positive sign means flow out from a node.
	 * Starting value for steady state solutions.
	 */
	private ActivePower activePower;
	/**
	 * Phase-to-phase nominal voltage.
	 */
	private Voltage nominalVoltage;
	/**
	 * Positive sequence Thevenin resistance.
	 */
	private Resistance r;
	/**
	 * Zero sequence Thevenin resistance.
	 */
	private Resistance r0;
	/**
	 * High voltage source reactive injection. Load sign convention is used, i.e.
	 * positive sign means flow out from a node.
	 * Starting value for steady state solutions.
	 */
	private ReactivePower reactivePower;
	/**
	 * Negative sequence Thevenin resistance.
	 */
	private Resistance rn;
	/**
	 * Phase angle of a-phase open circuit.
	 */
	private AngleRadians voltageAngle;
	/**
	 * Phase-to-phase open circuit voltage magnitude.
	 */
	private Voltage voltageMagnitude;
	/**
	 * Positive sequence Thevenin reactance.
	 */
	private Reactance x;
	/**
	 * Zero sequence Thevenin reactance.
	 */
	private Reactance x0;
	/**
	 * Negative sequence Thevenin reactance.
	 */
	private Reactance xn;

	public EnergySource(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public ActivePower getactivePower(){
		return activePower;
	}

	public EnergySchedulingType getEnergySchedulingType(){
		return EnergySchedulingType;
	}

	public Voltage getnominalVoltage(){
		return nominalVoltage;
	}

	public Resistance getr(){
		return r;
	}

	public Resistance getr0(){
		return r0;
	}

	public ReactivePower getreactivePower(){
		return reactivePower;
	}

	public Resistance getrn(){
		return rn;
	}

	public AngleRadians getvoltageAngle(){
		return voltageAngle;
	}

	public Voltage getvoltageMagnitude(){
		return voltageMagnitude;
	}

	public Reactance getx(){
		return x;
	}

	public Reactance getx0(){
		return x0;
	}

	public Reactance getxn(){
		return xn;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setactivePower(ActivePower newVal){
		activePower = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setEnergySchedulingType(EnergySchedulingType newVal){
		EnergySchedulingType = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setnominalVoltage(Voltage newVal){
		nominalVoltage = newVal;
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
	public void setreactivePower(ReactivePower newVal){
		reactivePower = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setrn(Resistance newVal){
		rn = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setvoltageAngle(AngleRadians newVal){
		voltageAngle = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setvoltageMagnitude(Voltage newVal){
		voltageMagnitude = newVal;
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

	/**
	 * 
	 * @param newVal
	 */
	public void setxn(Reactance newVal){
		xn = newVal;
	}

}