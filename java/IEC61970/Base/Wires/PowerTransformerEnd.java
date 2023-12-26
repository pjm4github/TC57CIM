package IEC61970.Base.Wires;

import IEC61970.Base.Domain.Susceptance;
import IEC61970.Base.Domain.Conductance;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Resistance;
import IEC61970.Base.Domain.ApparentPower;
import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.Reactance;

/**
 * A PowerTransformerEnd is associated with each Terminal of a PowerTransformer.
 * The impedance values r, r0, x, and x0 of a PowerTransformerEnd represents a
 * star equivalent as follows
 * 1) for a two Terminal PowerTransformer the high voltage (TransformerEnd.
 * endNumber=1) PowerTransformerEnd has non zero values on r, r0, x, and x0 while
 * the low voltage (TransformerEnd.endNumber=0) PowerTransformerEnd has zero
 * values for r, r0, x, and x0.
 * 2) for a three Terminal PowerTransformer the three PowerTransformerEnds
 * represents a star equivalent with each leg in the star represented by r, r0, x,
 * and x0 values.
 * 3) For a three Terminal transformer each PowerTransformerEnd shall have g, g0,
 * b and b0 values corresponding the no load losses distributed on the three
 * PowerTransformerEnds. The total no load loss shunt impedances may also be
 * placed at one of the PowerTransformerEnds, preferably the end numbered 1,
 * having the shunt values on end 1 is the preferred way.
 * 4) for a PowerTransformer with more than three Terminals the
 * PowerTransformerEnd impedance values cannot be used. Instead use the
 * TransformerMeshImpedance or split the transformer into multiple
 * PowerTransformers.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class PowerTransformerEnd extends TransformerEnd {

	/**
	 * Magnetizing branch susceptance (B mag).  The value can be positive or negative.
	 */
	public Susceptance b;
	/**
	 * Zero sequence magnetizing branch susceptance.
	 */
	public Susceptance b0;
	/**
	 * Kind of connection.
	 */
	public WindingConnection connectionKind;
	/**
	 * Magnetizing branch conductance.
	 */
	public Conductance g;
	/**
	 * Zero sequence magnetizing branch conductance (star-model).
	 */
	public Conductance g0;
	/**
	 * Terminal voltage phase angle displacement where 360 degrees are represented
	 * with clock hours. The valid values are 0 to 11. For example, for the secondary
	 * side end of a transformer with vector group code of 'Dyn11', specify the
	 * connection kind as wye with neutral and specify the phase angle of the clock as
	 * 11.  The clock value of the transformer end number specified as 1, is assumed
	 * to be zero.  Note the transformer end number is not assumed to be the same as
	 * the terminal sequence number.
	 */
	public Integer phaseAngleClock;
	/**
	 * Resistance (star-model) of the transformer end.
	 * The attribute shall be equal or greater than zero for non-equivalent
	 * transformers.
	 */
	public Resistance r;
	/**
	 * Zero sequence series resistance (star-model) of the transformer end.
	 */
	public Resistance r0;
	/**
	 * Normal apparent power rating.
	 * The attribute shall be a positive value. For a two-winding transformer the
	 * values for the high and low voltage sides shall be identical. 
	 */
	public ApparentPower ratedS;
	/**
	 * Rated voltage: phase-phase for three-phase windings, and either phase-phase or
	 * phase-neutral for single-phase windings.
	 * A high voltage side, as given by TransformerEnd.endNumber, shall have a ratedU
	 * that is greater or equal than ratedU for the lower voltage sides.
	 */
	public Voltage ratedU;
	/**
	 * Positive sequence series reactance (star-model) of the transformer end.
	 */
	public Reactance x;
	/**
	 * Zero sequence series reactance of the transformer end.
	 */
	public Reactance x0;

	public PowerTransformerEnd(){

	}
}//end PowerTransformerEnd