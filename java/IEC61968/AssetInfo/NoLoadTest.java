package IEC61968.AssetInfo;

import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.KiloActivePower;

/**
 * No-load test results determine core admittance parameters. They include
 * exciting current and core loss measurements from applying voltage to one
 * winding. The excitation may be positive sequence or zero sequence. The test may
 * be repeated at different voltages to measure saturation.
 * @author Tom
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class NoLoadTest extends TransformerTest {

	/**
	 * Voltage applied to the winding (end) during test.
	 */
	public Voltage energisedEndVoltage;
	/**
	 * Exciting current measured from a positive-sequence or single-phase excitation
	 * test.
	 */
	public PerCent excitingCurrent;
	/**
	 * Exciting current measured from a zero-sequence open-circuit excitation test.
	 */
	public PerCent excitingCurrentZero;
	/**
	 * Losses measured from a positive-sequence or single-phase excitation test.
	 */
	public KiloActivePower loss;
	/**
	 * Losses measured from a zero-sequence excitation test.
	 */
	public KiloActivePower lossZero;
	/**
	 * Transformer end that current is applied to in this no-load test.
	 */
	public TransformerEndInfo EnergisedEnd;

	public NoLoadTest(){

	}
}//end NoLoadTest