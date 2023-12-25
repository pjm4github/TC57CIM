

import TC57CIM.IEC61970.Base.Domain.CurrentFlow;

/**
 * A conductor, or group of conductors, with negligible impedance, that serve to
 * connect other conducting equipment within a single substation.
 * Voltage measurements are typically obtained from VoltageTransformers that are
 * connected to busbar sections. A bus bar section may have many physical
 * terminals but for analysis is modelled with exactly one logical terminal.
 * @author pmora
 * @updated 15-Dec-2023 1:39:41 PM
 */
public class BusbarSection extends Connector {

	/**
	 * Maximum allowable peak short-circuit current of busbar (Ipmax in the IEC 60909-
	 * 0).
	 * Mechanical limit of the busbar in the substation itself. Used for short circuit
	 * data exchange according to IEC 60909
	 */
	private CurrentFlow ipMax;
	/**
	 * A VoltageControlZone is controlled by a designated BusbarSection.
	 */
	private VoltageControlZone VoltageControlZone;

	public BusbarSection(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public CurrentFlow getipMax(){
		return ipMax;
	}

	public VoltageControlZone getVoltageControlZone(){
		return VoltageControlZone;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setipMax(CurrentFlow newVal){
		ipMax = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setVoltageControlZone(VoltageControlZone newVal){
		VoltageControlZone = newVal;
	}

}