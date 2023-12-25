package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.PerCent;
import TC57CIM.IEC61970.Base.Domain.Reactance;

/**
 * The non-linear phase tap changer describes the non-linear behavior of a phase
 * tap changer. This is a base class for the symmetrical and asymmetrical phase
 * tap changer models. The details of these models can be found in the IEC 61970-
 * 301 document.
 * @author SELAOST1
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public class PhaseTapChangerNonLinear extends PhaseTapChanger {

	/**
	 * The voltage step increment on the out of phase winding specified in percent of
	 * neutral voltage of the tap changer.
	 */
	public PerCent voltageStepIncrement;
	/**
	 * The reactance depend on the tap position according to a "u" shaped curve. The
	 * maximum reactance (xMax) appear at the low and high tap positions.
	 */
	public Reactance xMax;
	/**
	 * The reactance depend on the tap position according to a "u" shaped curve. The
	 * minimum reactance (xMin) appear at the mid tap position.
	 */
	public Reactance xMin;

	public PhaseTapChangerNonLinear(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}