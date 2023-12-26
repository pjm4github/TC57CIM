package IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics;

import IEC61970.Base.Domain.Float;

/**
 * All synchronous machine detailed types use a subset of the same data parameters
 * and input/output variables.
 * The several variations differ in the following ways:
 * <ul>
 * 	<li>The number of  equivalent windings that are included</li>
 * 	<li>The way in which saturation is incorporated into the model.</li>
 * 	<li>Whether or not "subtransient saliency" (<b>X''q</b> not = <b>X''d</b>) is
 * represented.</li>
 * </ul>
 * <b>Note:</b> It is not necessary for each simulation tool to have separate
 * models for each of the model types.  The same model can often be used for
 * several types by alternative logic within the model.  Also, differences in
 * saturation representation may not result in significant model performance
 * differences so model substitutions are often acceptable.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class SynchronousMachineDetailed extends SynchronousMachineDynamics {

	/**
	 * Ratio (Exciter voltage/Generator voltage) of Efd bases of exciter and generator
	 * models. Typical Value = 1.
	 */
	public Float efdBaseRatio;
	/**
	 * Excitation base system mode. It should be equal to the value of WLMDV given by
	 * the user. WLMDV is the per unit ratio between the field voltage and the
	 * excitation current: Efd = WLMDV*Ifd. Typical Value = ifag.
	 */
	public IfdBaseKind ifdBaseType;
	/**
	 * Q-axis saturation factor at 120% of rated terminal voltage (S12q) (>=S1q).
	 * Typical Value = 0.12.
	 */
	public Float saturationFactor120QAxis;
	/**
	 * Q-axis saturation factor at rated terminal voltage (S1q) (>= 0). Typical Value
	 * = 0.02.
	 */
	public Float saturationFactorQAxis;

	public SynchronousMachineDetailed(){

	}
}//end SynchronousMachineDetailed