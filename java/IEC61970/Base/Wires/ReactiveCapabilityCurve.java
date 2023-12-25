

import TC57CIM.IEC61970.Base.Domain.Temperature;
import TC57CIM.IEC61970.Base.Domain.Pressure;
import TC57CIM.IEC61970.Base.Equivalents.EquivalentInjection;

/**
 * Reactive power rating envelope versus the synchronous machine's active power,
 * in both the generating and motoring modes. For each active power value there is
 * a corresponding high and low reactive power limit  value. Typically there will
 * be a separate curve for each coolant condition, such as hydrogen pressure.  The
 * Y1 axis values represent reactive minimum and the Y2 axis values represent
 * reactive maximum.
 * @author pmora
 * @updated 15-Dec-2023 1:39:42 PM
 */
public class ReactiveCapabilityCurve {

	/**
	 * The machine's coolant temperature (e.g., ambient air or stator circulating
	 * water).
	 */
	private Temperature coolantTemperature;
	/**
	 * The hydrogen coolant pressure
	 */
	private Pressure hydrogenPressure;
	/**
	 * Synchronous machines using this curve as default.
	 */
	private SynchronousMachine InitiallyUsedBySynchronousMachines;
	/**
	 * Synchronous machines using this curve.
	 */
	private SynchronousMachine SynchronousMachines;

	public ReactiveCapabilityCurve(){

	}

	public void finalize() throws Throwable {

	}

	public Temperature getcoolantTemperature(){
		return coolantTemperature;
	}

	public EquivalentInjection getEquivalentInjection(){
		return EquivalentInjection;
	}

	public Pressure gethydrogenPressure(){
		return hydrogenPressure;
	}

	public SynchronousMachine getInitiallyUsedBySynchronousMachines(){
		return InitiallyUsedBySynchronousMachines;
	}

	public SynchronousMachine getSynchronousMachines(){
		return SynchronousMachines;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setcoolantTemperature(Temperature newVal){
		coolantTemperature = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setEquivalentInjection(EquivalentInjection newVal){
		EquivalentInjection = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void sethydrogenPressure(Pressure newVal){
		hydrogenPressure = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setInitiallyUsedBySynchronousMachines(SynchronousMachine newVal){
		InitiallyUsedBySynchronousMachines = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setSynchronousMachines(SynchronousMachine newVal){
		SynchronousMachines = newVal;
	}

}