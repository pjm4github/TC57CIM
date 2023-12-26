package IEC61970.Base.Wires;

import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.Reactance;

/**
 * A tunable impedance device normally used to offset line charging during single
 * line faults in an ungrounded section of network.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PetersenCoil extends EarthFaultCompensator {

	/**
	 * The mode of operation of the Petersen coil.
	 */
	public PetersenCoilModeKind mode;
	/**
	 * The nominal voltage for which the coil is designed.
	 */
	public Voltage nominalU;
	/**
	 * The offset current that the Petersen coil controller is operating from the
	 * resonant point.  This is normally a fixed amount for which the controller is
	 * configured and could be positive or negative.  Typically 0 to 60 Amperes
	 * depending on voltage and resonance conditions.
	 */
	public CurrentFlow offsetCurrent;
	/**
	 * The control current used to control the Petersen coil also known as the
	 * position current.  Typically in the range of 20-200mA.
	 */
	public CurrentFlow positionCurrent;
	/**
	 * The maximum reactance. 
	 */
	public Reactance xGroundMax;
	/**
	 * The minimum reactance.
	 */
	public Reactance xGroundMin;
	/**
	 * The nominal reactance.  This is the operating point (normally over
	 * compensation) that is defined based on the resonance point in the healthy
	 * network condition.  The impedance is calculated based on nominal voltage
	 * divided by position current.
	 */
	public Reactance xGroundNominal;

	public PetersenCoil(){

	}
}//end PetersenCoil