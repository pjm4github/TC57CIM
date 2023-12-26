package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * The class models a look up table for the purpose of wind standard models.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindDynamicsLookupTable extends IdentifiedObject {

	/**
	 * Input value (x) for the lookup table function.
	 */
	public Float input;
	/**
	 * Type of the lookup table function.
	 */
	public WindLookupTableFunctionKind lookupTableFunctionType;
	/**
	 * Output value (y) for the lookup table function.
	 */
	public Float output;
	/**
	 * Sequence numbers of the pairs of the input (x) and the output (y) of the lookup
	 * table function.
	 */
	public Integer sequence;
	/**
	 * The frequency and active power wind plant control model with which this wind
	 * dynamics lookup table is associated.
	 */
	public WindPlantFreqPcontrolIEC WindPlantFreqPcontrolIEC;
	/**
	 * The voltage and reactive power wind plant control model with which this wind
	 * dynamics lookup table is associated.
	 */
	public WindPlantReactiveControlIEC WindPlantReactiveControlIEC;
	/**
	 * The grid protection model with which this wind dynamics lookup table is
	 * associated.
	 */
	public WindProtectionIEC WindProtectionIEC;
	/**
	 * The QP and QU limitation model with which this wind dynamics lookup table is
	 * associated.
	 */
	public WindContQPQULimIEC WindContQPQULimIEC;
	/**
	 * The current control limitation model with which this wind dynamics lookup table
	 * is associated.
	 */
	public WindContCurrLimIEC WindContCurrLimIEC;
	/**
	 * The P control type 3 model with which this wind dynamics lookup table is
	 * associated.
	 */
	public WindContPType3IEC WindContPType3IEC;
	/**
	 * The rotor resistance control model with which this wind dynamics lookup table
	 * is associated.
	 */
	public WindContRotorRIEC WindContRotorRIEC;
	/**
	 * The pitch control power model with which this wind dynamics lookup table is
	 * associated.
	 */
	public WindPitchContPowerIEC WindPitchContPowerIEC;
	/**
	 * The generator type 3B model with which this wind dynamics lookup table is
	 * associated.
	 */
	public WindGenType3bIEC WindGenType3bIEC;

	public WindDynamicsLookupTable(){

	}
}//end WindDynamicsLookupTable