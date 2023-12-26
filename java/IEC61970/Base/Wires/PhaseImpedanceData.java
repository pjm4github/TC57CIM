package IEC61970.Base.Wires;

import IEC61970.Base.Domain.SusceptancePerLength;
import IEC61970.Base.Domain.ConductancePerLength;
import IEC61970.Base.Domain.ResistancePerLength;
import IEC61970.Base.Domain.ReactancePerLength;

/**
 * Impedance and conductance matrix element values.
 * The diagonal elements are described by the elements having the same toPhase and
 * fromPhase value and the off diagonal elements have different toPhase and
 * fromPhase values.
 * @author Tom
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PhaseImpedanceData {

	/**
	 * Susceptance matrix element value, per length of unit.
	 */
	public SusceptancePerLength b;
	/**
	 * Refer to the class description.
	 */
	public SinglePhaseKind fromPhase;
	/**
	 * Conductance matrix element value, per length of unit.
	 */
	public ConductancePerLength g;
	/**
	 * Resistance matrix element value, per length of unit.
	 */
	public ResistancePerLength r;
	/**
	 * Refer to the class description.
	 */
	public SinglePhaseKind toPhase;
	/**
	 * Reactance matrix element value, per length of unit.
	 */
	public ReactancePerLength x;

	public PhaseImpedanceData(){

	}
}//end PhaseImpedanceData