

import TC57CIM.IEC61970.Base.Domain.Seconds;
import TC57CIM.IEC61970.Base.Domain.ReactivePower;
import TC57CIM.IEC61970.Base.Domain.ActivePower;
import TC57CIM.IEC61970.Base.Domain.Resistance;
import TC57CIM.IEC61970.Base.Domain.Reactance;
import TC57CIM.IEC61970.Base.Domain.CurrentFlow;
import TC57CIM.IEC61970.Base.Domain.Voltage;
import TC57CIM.IEC61970.Base.Domain.PerCent;
import TC57CIM.IEC61970.Base.Domain.PU;

/**
 * An electromechanical device that operates with shaft rotating synchronously
 * with the network. It is a single machine operating either as a generator or
 * synchronous condenser or pump.
 * @author pmora
 * @updated 15-Dec-2023 1:39:42 PM
 */
public class SynchronousMachine extends RotatingMachine {

	/**
	 * Time delay required when switching from Automatic Voltage Regulation (AVR) to
	 * Manual for a lagging MVAr violation.
	 */
	private Seconds aVRToManualLag;
	/**
	 * Time delay required when switching from Automatic Voltage Regulation (AVR) to
	 * Manual for a leading MVAr violation.
	 */
	private Seconds aVRToManualLead;
	/**
	 * Default base reactive power value. This value represents the initial reactive
	 * power that can be used by any application function.
	 */
	private ReactivePower baseQ;
	/**
	 * Active power consumed when in condenser mode operation.
	 */
	private ActivePower condenserP;
	/**
	 * Temperature or pressure of coolant medium
	 */
	private float coolantCondition;
	/**
	 * Method of cooling the machine.
	 */
	private CoolantType coolantType;
	/**
	 * Indicates whether or not the generator is earthed. Used for short circuit data
	 * exchange according to IEC 60909
	 */
	private boolean earthing;
	/**
	 * Generator star point earthing resistance (Re). Used for short circuit data
	 * exchange according to IEC 60909
	 */
	private Resistance earthingStarPointR;
	/**
	 * Generator star point earthing reactance (Xe). Used for short circuit data
	 * exchange according to IEC 60909
	 */
	private Reactance earthingStarPointX;
	/**
	 * Steady-state short-circuit current (in A for the profile) of generator with
	 * compound excitation during 3-phase short circuit.
	 * - Ikk=0: Generator with no compound excitation.
	 * - Ikk?0: Generator with compound excitation.
	 * Ikk is used to calculate the minimum steady-state short-circuit current for
	 * generators with compound excitation
	 * (Section 4.6.1.2 in the IEC 60909-0)
	 * Used only for single fed short circuit on a generator. (Section 4.3.4.2. in the
	 * IEC 60909-0)
	 */
	private CurrentFlow ikk;
	/**
	 * Time delay required when switching from Manual to Automatic Voltage Regulation.
	 * This value is used in the accelerating power reference frame for powerflow
	 * solutions
	 */
	private Seconds manualToAVR;
	/**
	 * Maximum reactive power limit. This is the maximum (nameplate) limit for the
	 * unit.
	 */
	private ReactivePower maxQ;
	/**
	 * Maximum voltage limit for the unit.
	 */
	private Voltage maxU;
	/**
	 * Minimum reactive power limit for the unit.
	 */
	private ReactivePower minQ;
	/**
	 * Minimum voltage  limit for the unit.
	 */
	private Voltage minU;
	/**
	 * Factor to calculate the breaking current (Section 4.5.2.1 in the IEC 60909-0).
	 * Used only for single fed short circuit on a generator (Section 4.3.4.2. in the
	 * IEC 60909-0).
	 */
	private float mu;
	/**
	 * Current mode of operation.
	 */
	private SynchronousMachineOperatingMode operatingMode;
	/**
	 * Part of the coordinated reactive control that comes from this machine. The
	 * attribute is used as a participation factor not necessarily summing up to 100%
	 * for the participating devices in the control.
	 */
	private PerCent qPercent;
	/**
	 * Equivalent resistance (RG) of generator. RG is considered for the calculation
	 * of all currents, except for the calculation of the peak current ip. Used for
	 * short circuit data exchange according to IEC 60909
	 */
	private Resistance r;
	/**
	 * Zero sequence resistance of the synchronous machine.
	 */
	private Resistance r0;
	/**
	 * Negative sequence resistance.
	 */
	private Resistance r2;
	/**
	 * Priority of unit for use as powerflow voltage phase angle reference bus
	 * selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and
	 * so on.
	 */
	private int referencePriority;
	/**
	 * Direct-axis subtransient reactance saturated, also known as Xd"sat.
	 */
	private PU satDirectSubtransX;
	/**
	 * Direct-axes saturated synchronous reactance (xdsat); reciprocal of short-
	 * circuit ration. Used for short circuit data exchange, only for single fed short
	 * circuit on a generator. (Section 4.3.4.2. in the IEC 60909-0).
	 */
	private PU satDirectSyncX;
	/**
	 * Saturated Direct-axis transient reactance. The attribute is primarily used for
	 * short circuit calculations according to ANSI.
	 */
	private PU satDirectTransX;
	/**
	 * Type of rotor, used by short circuit applications, only for single fed short
	 * circuit according to IEC 60909.
	 */
	private ShortCircuitRotorKind shortCircuitRotorType;
	/**
	 * Modes that this synchronous machine can operate in.
	 */
	private SynchronousMachineKind type;
	/**
	 * Range of generator voltage regulation (PG in the IEC 60909-0) used for
	 * calculation of the impedance correction factor KG defined in IEC 60909-0
	 * This attribute is used to describe the operating voltage of the generating unit.
	 */
	private PerCent voltageRegulationRange;
	/**
	 * Zero sequence reactance of the synchronous machine.
	 */
	private Reactance x0;
	/**
	 * Negative sequence reactance.
	 */
	private Reactance x2;

	public SynchronousMachine(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public Seconds getaVRToManualLag(){
		return aVRToManualLag;
	}

	public Seconds getaVRToManualLead(){
		return aVRToManualLead;
	}

	public ReactivePower getbaseQ(){
		return baseQ;
	}

	public ActivePower getcondenserP(){
		return condenserP;
	}

	public float getcoolantCondition(){
		return coolantCondition;
	}

	public CoolantType getcoolantType(){
		return coolantType;
	}

	public boolean getearthing(){
		return earthing;
	}

	public Resistance getearthingStarPointR(){
		return earthingStarPointR;
	}

	public Reactance getearthingStarPointX(){
		return earthingStarPointX;
	}

	public CurrentFlow getikk(){
		return ikk;
	}

	public Seconds getmanualToAVR(){
		return manualToAVR;
	}

	public ReactivePower getmaxQ(){
		return maxQ;
	}

	public Voltage getmaxU(){
		return maxU;
	}

	public ReactivePower getminQ(){
		return minQ;
	}

	public Voltage getminU(){
		return minU;
	}

	public float getmu(){
		return mu;
	}

	public SynchronousMachineOperatingMode getoperatingMode(){
		return operatingMode;
	}

	public PerCent getqPercent(){
		return qPercent;
	}

	public Resistance getr(){
		return r;
	}

	public Resistance getr0(){
		return r0;
	}

	public Resistance getr2(){
		return r2;
	}

	public int getreferencePriority(){
		return referencePriority;
	}

	public PU getsatDirectSubtransX(){
		return satDirectSubtransX;
	}

	public PU getsatDirectSyncX(){
		return satDirectSyncX;
	}

	public PU getsatDirectTransX(){
		return satDirectTransX;
	}

	public ShortCircuitRotorKind getshortCircuitRotorType(){
		return shortCircuitRotorType;
	}

	public SynchronousMachineKind gettype(){
		return type;
	}

	public PerCent getvoltageRegulationRange(){
		return voltageRegulationRange;
	}

	public Reactance getx0(){
		return x0;
	}

	public Reactance getx2(){
		return x2;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setaVRToManualLag(Seconds newVal){
		aVRToManualLag = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setaVRToManualLead(Seconds newVal){
		aVRToManualLead = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setbaseQ(ReactivePower newVal){
		baseQ = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setcondenserP(ActivePower newVal){
		condenserP = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setcoolantCondition(float newVal){
		coolantCondition = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setcoolantType(CoolantType newVal){
		coolantType = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setearthing(boolean newVal){
		earthing = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setearthingStarPointR(Resistance newVal){
		earthingStarPointR = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setearthingStarPointX(Reactance newVal){
		earthingStarPointX = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setikk(CurrentFlow newVal){
		ikk = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setmanualToAVR(Seconds newVal){
		manualToAVR = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setmaxQ(ReactivePower newVal){
		maxQ = newVal;
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
	public void setminQ(ReactivePower newVal){
		minQ = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setminU(Voltage newVal){
		minU = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setmu(float newVal){
		mu = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setoperatingMode(SynchronousMachineOperatingMode newVal){
		operatingMode = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setqPercent(PerCent newVal){
		qPercent = newVal;
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
	public void setr2(Resistance newVal){
		r2 = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setreferencePriority(int newVal){
		referencePriority = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setsatDirectSubtransX(PU newVal){
		satDirectSubtransX = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setsatDirectSyncX(PU newVal){
		satDirectSyncX = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setsatDirectTransX(PU newVal){
		satDirectTransX = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setshortCircuitRotorType(ShortCircuitRotorKind newVal){
		shortCircuitRotorType = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void settype(SynchronousMachineKind newVal){
		type = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setvoltageRegulationRange(PerCent newVal){
		voltageRegulationRange = newVal;
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
	public void setx2(Reactance newVal){
		x2 = newVal;
	}

}