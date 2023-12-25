


/**
 * A pre-established pattern over time for a controlled variable, e.g., busbar
 * voltage.
 * @author pmora
 * @updated 15-Dec-2023 1:39:42 PM
 */
public class RegulationSchedule {

	/**
	 * Regulating controls that have this Schedule.
	 */
	private RegulatingControl RegulatingControl;
	/**
	 * A VoltageControlZone may have a  voltage regulation schedule.
	 */
	private VoltageControlZone VoltageControlZones;

	public RegulationSchedule(){

	}

	public void finalize() throws Throwable {

	}

	public RegulatingControl getRegulatingControl(){
		return RegulatingControl;
	}

	public VoltageControlZone getVoltageControlZones(){
		return VoltageControlZones;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setRegulatingControl(RegulatingControl newVal){
		RegulatingControl = newVal;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setVoltageControlZones(VoltageControlZone newVal){
		VoltageControlZones = newVal;
	}

}