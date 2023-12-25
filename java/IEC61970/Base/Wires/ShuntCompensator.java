

import TC57CIM.IEC61970.Base.Domain.Seconds;
import TC57CIM.IEC61970.Base.Domain.Voltage;
import TC57CIM.IEC61970.Base.Domain.DateTime;
import TC57CIM.IEC61970.Base.Domain.VoltagePerReactivePower;

/**
 * A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors.
 * A section of a shunt compensator is an individual capacitor or reactor.  A
 * negative value for reactivePerSection indicates that the compensator is a
 * reactor. ShuntCompensator is a single terminal device.  Ground is implied.
 * @author pmora
 * @updated 15-Dec-2023 1:39:42 PM
 */
public class ShuntCompensator extends RegulatingCondEq {

	/**
	 * Time delay required for the device to be connected or disconnected by automatic
	 * voltage regulation (AVR).
	 */
	private Seconds aVRDelay;
	/**
	 * Used for Yn and Zn connections. True if the neutral is solidly grounded.
	 */
	private boolean grounded;
	/**
	 * The maximum number of sections that may be switched in. 
	 */
	private int maximumSections;
	/**
	 * The voltage at which the nominal reactive power may be calculated. This should
	 * normally be within 10% of the voltage at which the capacitor is connected to
	 * the network.
	 */
	private Voltage nomU;
	/**
	 * The normal number of sections switched in.
	 */
	private int normalSections;
	/**
	 * The type of phase connection, such as wye or delta.
	 */
	private PhaseShuntConnectionKind phaseConnection;
	/**
	 * Shunt compensator sections in use.
	 * Starting value for steady state solution. Non integer values are allowed to
	 * support continuous variables. The reasons for continuous value are to support
	 * study cases where no discrete shunt compensators has yet been designed, a
	 * solutions where a narrow voltage band force the sections to oscillate or
	 * accommodate for a continuous solution as input.
	 */
	private float sections;
	/**
	 * The switch on count since the capacitor count was last reset or initialized.
	 */
	private int switchOnCount;
	/**
	 * The date and time when the capacitor bank was last switched on.
	 */
	private DateTime switchOnDate;
	/**
	 * Voltage sensitivity required for the device to regulate the bus voltage, in
	 * voltage/reactive power.
	 */
	private VoltagePerReactivePower voltageSensitivity;
	/**
	 * The individual phases models for the shunt compensator.
	 */
	private ShuntCompensatorPhase ShuntCompensatorPhase;

	public ShuntCompensator(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public Seconds getaVRDelay(){
		return aVRDelay;
	}

	public boolean getgrounded(){
		return grounded;
	}

	public int getmaximumSections(){
		return maximumSections;
	}

	public Voltage getnomU(){
		return nomU;
	}

	public int getnormalSections(){
		return normalSections;
	}

	public PhaseShuntConnectionKind getphaseConnection(){
		return phaseConnection;
	}

	public float getsections(){
		return sections;
	}

	public ShuntCompensatorPhase getShuntCompensatorPhase(){
		return ShuntCompensatorPhase;
	}

	public int getswitchOnCount(){
		return switchOnCount;
	}

	public DateTime getswitchOnDate(){
		return switchOnDate;
	}

	public VoltagePerReactivePower getvoltageSensitivity(){
		return voltageSensitivity;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setaVRDelay(Seconds newVal){
		aVRDelay = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setgrounded(boolean newVal){
		grounded = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setmaximumSections(int newVal){
		maximumSections = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setnomU(Voltage newVal){
		nomU = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setnormalSections(int newVal){
		normalSections = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setphaseConnection(PhaseShuntConnectionKind newVal){
		phaseConnection = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setsections(float newVal){
		sections = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setShuntCompensatorPhase(ShuntCompensatorPhase newVal){
		ShuntCompensatorPhase = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setswitchOnCount(int newVal){
		switchOnCount = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setswitchOnDate(DateTime newVal){
		switchOnDate = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setvoltageSensitivity(VoltagePerReactivePower newVal){
		voltageSensitivity = newVal;
	}

}