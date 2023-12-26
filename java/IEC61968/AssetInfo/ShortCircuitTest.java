package IEC61968.AssetInfo;

import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Impedance;
import IEC61970.Base.Domain.KiloActivePower;
import IEC61970.Base.Domain.ApparentPower;
import IEC61970.Base.Domain.PerCent;

/**
 * Short-circuit test results determine mesh impedance parameters. They include
 * load losses and leakage impedances. For three-phase windings, the excitation
 * can be a positive sequence (the default) or a zero sequence. There shall be at
 * least one grounded winding.
 * @author Tom
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class ShortCircuitTest extends TransformerTest {

	/**
	 * Short circuit current..
	 */
	public CurrentFlow current;
	/**
	 * Tap step number for the energised end of the test pair.
	 */
	public Integer energisedEndStep;
	/**
	 * Tap step number for the grounded end of the test pair.
	 */
	public Integer groundedEndStep;
	/**
	 * Leakage impedance measured from a positive-sequence or single-phase short-
	 * circuit test.
	 */
	public Impedance leakageImpedance;
	/**
	 * Leakage impedance measured from a zero-sequence short-circuit test.
	 */
	public Impedance leakageImpedanceZero;
	/**
	 * Load losses from a positive-sequence or single-phase short-circuit test.
	 */
	public KiloActivePower loss;
	/**
	 * Load losses from a zero-sequence short-circuit test.
	 */
	public KiloActivePower lossZero;
	/**
	 * Short circuit apparent power.
	 */
	public ApparentPower power;
	/**
	 * Short circuit voltage..
	 */
	public PerCent voltage;
	/**
	 * All ends short-circuited in this short-circuit test.
	 */
	public TransformerEndInfo GroundedEnds;
	/**
	 * Transformer end that voltage is applied to in this short-circuit test. The test
	 * voltage is chosen to induce rated current in the energised end.
	 */
	public TransformerEndInfo EnergisedEnd;

	public ShortCircuitTest(){

	}
}//end ShortCircuitTest