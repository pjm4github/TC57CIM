package IEC61968.AssetInfo;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.AngleDegrees;

/**
 * Open-circuit test results verify winding turn ratios and phase shifts. They
 * include induced voltage and phase shift measurements on open-circuit windings,
 * with voltage applied to the energised end. For three-phase windings, the
 * excitation can be a positive sequence (the default) or a zero sequence.
 * @author Tom
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class OpenCircuitTest extends TransformerTest {

	/**
	 * Tap step number for the energised end of the test pair.
	 */
	public Integer energisedEndStep;
	/**
	 * Voltage applied to the winding (end) during test.
	 */
	public Voltage energisedEndVoltage;
	/**
	 * Tap step number for the open end of the test pair.
	 */
	public Integer openEndStep;
	/**
	 * Voltage measured at the open-circuited end, with the energised end set to rated
	 * voltage and all other ends open.
	 */
	public Voltage openEndVoltage;
	/**
	 * Phase shift measured at the open end with the energised end set to rated
	 * voltage and all other ends open.
	 */
	public AngleDegrees phaseShift;
	/**
	 * Transformer end measured for induced voltage and angle in this open-circuit
	 * test.
	 */
	public TransformerEndInfo OpenEnd;
	/**
	 * Transformer end that current is applied to in this open-circuit test.
	 */
	public TransformerEndInfo EnergisedEnd;

	public OpenCircuitTest(){

	}
}//end OpenCircuitTest