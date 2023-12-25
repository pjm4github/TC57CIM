package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.PerCent;

/**
 * A tap changer that changes the voltage ratio impacting the voltage magnitude
 * but not the phase angle across the transformer.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:29 PM
 */
public class RatioTapChanger extends TapChanger {

	/**
	 * Tap step increment, in per cent of neutral voltage, per step position.
	 */
	public PerCent stepVoltageIncrement;
	/**
	 * Specifies the regulation control mode (voltage or reactive) of the
	 * RatioTapChanger.
	 */
	public TransformerControlMode tculControlMode;
	/**
	 * The tap ratio table for this ratio  tap changer.
	 */
	public RatioTapChangerTable RatioTapChangerTable;

	public RatioTapChanger(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}