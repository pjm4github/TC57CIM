

import TC57CIM.IEC61970.Base.Domain.Reactance;
import TC57CIM.IEC61970.Base.Domain.ReactivePower;
import TC57CIM.IEC61970.Base.Domain.VoltagePerReactivePower;
import TC57CIM.IEC61970.Base.Domain.Voltage;

/**
 * A facility for providing variable and controllable shunt reactive power. The
 * SVC typically consists of a stepdown transformer, filter, thyristor-controlled
 * reactor, and thyristor-switched capacitor arms.
 * 
 * The SVC may operate in fixed MVar output mode or in voltage control mode. When
 * in voltage control mode, the output of the SVC will be proportional to the
 * deviation of voltage at the controlled bus from the voltage setpoint.  The SVC
 * characteristic slope defines the proportion.  If the voltage at the controlled
 * bus is equal to the voltage setpoint, the SVC MVar output is zero.
 * @author pmora
 * @updated 15-Dec-2023 1:39:42 PM
 */
public class StaticVarCompensator extends RegulatingCondEq {

	/**
	 * Maximum available capacitive reactance.
	 */
	private Reactance capacitiveRating;
	/**
	 * Maximum available inductive reactance.
	 */
	private Reactance inductiveRating;
	/**
	 * Reactive power injection. Load sign convention is used, i.e. positive sign
	 * means flow out from a node.
	 * Starting value for a steady state solution.
	 */
	private ReactivePower q;
	/**
	 * The characteristics slope of an SVC defines how the reactive power output
	 * changes in proportion to the difference between the regulated bus voltage and
	 * the voltage setpoint.
	 */
	private VoltagePerReactivePower slope;
	/**
	 * SVC control mode.
	 */
	private SVCControlMode sVCControlMode;
	/**
	 * The reactive power output of the SVC is proportional to the difference between
	 * the voltage at the regulated bus and the voltage setpoint.  When the regulated
	 * bus voltage is equal to the voltage setpoint, the reactive power output is zero.
	 */
	private Voltage voltageSetPoint;

	public StaticVarCompensator(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public Reactance getcapacitiveRating(){
		return capacitiveRating;
	}

	public Reactance getinductiveRating(){
		return inductiveRating;
	}

	public ReactivePower getq(){
		return q;
	}

	public VoltagePerReactivePower getslope(){
		return slope;
	}

	public SVCControlMode getsVCControlMode(){
		return sVCControlMode;
	}

	public Voltage getvoltageSetPoint(){
		return voltageSetPoint;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setcapacitiveRating(Reactance newVal){
		capacitiveRating = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setinductiveRating(Reactance newVal){
		inductiveRating = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setq(ReactivePower newVal){
		q = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setslope(VoltagePerReactivePower newVal){
		slope = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setsVCControlMode(SVCControlMode newVal){
		sVCControlMode = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setvoltageSetPoint(Voltage newVal){
		voltageSetPoint = newVal;
	}

}