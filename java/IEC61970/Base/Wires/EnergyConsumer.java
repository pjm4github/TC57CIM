

import TC57CIM.IEC61970.Base.Domain.ActivePower;
import TC57CIM.IEC61970.Base.Domain.PerCent;
import TC57CIM.IEC61970.Base.Domain.ReactivePower;
import TC57CIM.IEC61970.Base.LoadModel.LoadResponseCharacteristic;

/**
 * Generic user of energy - a  point of consumption on the power system model.
 * @author pmora
 * @updated 15-Dec-2023 1:39:41 PM
 */
public class EnergyConsumer extends EnergyConnection {

	/**
	 * Number of individual customers represented by this demand.
	 */
	private int customerCount;
	/**
	 * Used for Yn and Zn connections. True if the neutral is solidly grounded.
	 */
	private boolean grounded;
	/**
	 * Active power of the load. Load sign convention is used, i.e. positive sign
	 * means flow out from a node.
	 * For voltage dependent loads the value is at rated voltage.
	 * Starting value for a steady state solution.
	 */
	private ActivePower p;
	/**
	 * Active power of the load that is a fixed quantity. Load sign convention is used,
	 * i.e. positive sign means flow out from a node.
	 */
	private ActivePower pfixed;
	/**
	 * Fixed active power as per cent of load group fixed active power. Load sign
	 * convention is used, i.e. positive sign means flow out from a node.
	 */
	private PerCent pfixedPct;
	/**
	 * The type of phase connection, such as wye or delta.
	 */
	private PhaseShuntConnectionKind phaseConnection;
	/**
	 * Reactive power of the load. Load sign convention is used, i.e. positive sign
	 * means flow out from a node.
	 * For voltage dependent loads the value is at rated voltage.
	 * Starting value for a steady state solution.
	 */
	private ReactivePower q;
	/**
	 * Reactive power of the load that is a fixed quantity. Load sign convention is
	 * used, i.e. positive sign means flow out from a node.
	 */
	private ReactivePower qfixed;
	/**
	 * Fixed reactive power as per cent of load group fixed reactive power. Load sign
	 * convention is used, i.e. positive sign means flow out from a node.
	 */
	private PerCent qfixedPct;
	/**
	 * The individual phase models for this energy consumer.
	 */
	private EnergyConsumerPhase EnergyConsumerPhase;

	public EnergyConsumer(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public int getcustomerCount(){
		return customerCount;
	}

	public EnergyConsumerPhase getEnergyConsumerPhase(){
		return EnergyConsumerPhase;
	}

	public boolean getgrounded(){
		return grounded;
	}

	public LoadResponseCharacteristic getLoadResponse(){
		return LoadResponse;
	}

	public ActivePower getp(){
		return p;
	}

	public ActivePower getpfixed(){
		return pfixed;
	}

	public PerCent getpfixedPct(){
		return pfixedPct;
	}

	public PhaseShuntConnectionKind getphaseConnection(){
		return phaseConnection;
	}

	public ReactivePower getq(){
		return q;
	}

	public ReactivePower getqfixed(){
		return qfixed;
	}

	public PerCent getqfixedPct(){
		return qfixedPct;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setcustomerCount(int newVal){
		customerCount = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setEnergyConsumerPhase(EnergyConsumerPhase newVal){
		EnergyConsumerPhase = newVal;
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
	public void setLoadResponse(LoadResponseCharacteristic newVal){
		LoadResponse = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setp(ActivePower newVal){
		p = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setpfixed(ActivePower newVal){
		pfixed = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setpfixedPct(PerCent newVal){
		pfixedPct = newVal;
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
	public void setq(ReactivePower newVal){
		q = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setqfixed(ReactivePower newVal){
		qfixed = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setqfixedPct(PerCent newVal){
		qfixedPct = newVal;
	}

}