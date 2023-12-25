package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.Voltage;
import TC57CIM.IEC61970.Base.Domain.Boolean;
import TC57CIM.IEC61970.Base.Domain.Resistance;
import TC57CIM.IEC61970.Base.Domain.Reactance;

/**
 * Describes behavior specific to tap changers, e.g. how the voltage at the end of
 * a line varies with the load level and compensation of the voltage drop by tap
 * adjustment.
 * @author Tom
 * @version 1.0
 * @created 15-Dec-2023 4:38:29 PM
 */
public class TapChangerControl extends RegulatingControl {

	/**
	 * Maximum allowed regulated voltage on the PT secondary, regardless of line drop
	 * compensation. Sometimes referred to as first-house protection.
	 */
	public Voltage limitVoltage;
	/**
	 * If true, the line drop compensation is to be applied.
	 */
	public Boolean lineDropCompensation;
	/**
	 * Line drop compensator resistance setting for normal (forward) power flow.
	 */
	public Resistance lineDropR;
	/**
	 * Line drop compensator reactance setting for normal (forward) power flow.
	 */
	public Reactance lineDropX;
	/**
	 * Line drop compensator resistance setting for reverse power flow.
	 */
	public Resistance reverseLineDropR;
	/**
	 * Line drop compensator reactance setting for reverse power flow.
	 */
	public Reactance reverseLineDropX;

	public TapChangerControl(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}