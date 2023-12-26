package IEC61970.Base.Wires;

import IEC61970.Base.Domain.SusceptancePerLength;
import IEC61970.Base.Domain.ConductancePerLength;
import IEC61970.Base.Domain.ResistancePerLength;
import IEC61970.Base.Domain.ReactancePerLength;

/**
 * Sequence impedance and admittance parameters per unit length, for transposed
 * lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase
 * lines, define x=xs-xm and x0=xs+xm.
 * @author Tom
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PerLengthSequenceImpedance extends PerLengthImpedance {

	/**
	 * Zero sequence shunt (charging) susceptance, per unit of length.
	 */
	public SusceptancePerLength b0ch;
	/**
	 * Positive sequence shunt (charging) susceptance, per unit of length.
	 */
	public SusceptancePerLength bch;
	/**
	 * Zero sequence shunt (charging) conductance, per unit of length.
	 */
	public ConductancePerLength g0ch;
	/**
	 * Positive sequence shunt (charging) conductance, per unit of length.
	 */
	public ConductancePerLength gch;
	/**
	 * Positive sequence series resistance, per unit of length.
	 */
	public ResistancePerLength r;
	/**
	 * Zero sequence series resistance, per unit of length.
	 */
	public ResistancePerLength r0;
	/**
	 * Positive sequence series reactance, per unit of length.
	 */
	public ReactancePerLength x;
	/**
	 * Zero sequence series reactance, per unit of length.
	 */
	public ReactancePerLength x0;

	public PerLengthSequenceImpedance(){

	}
}//end PerLengthSequenceImpedance