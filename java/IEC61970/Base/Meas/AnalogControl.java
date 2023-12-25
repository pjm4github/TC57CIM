package TC57CIM.IEC61970.Base.Meas;

import TC57CIM.IEC61970.Base.Domain.Float;

/**
 * An analog control used for supervisory control.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class AnalogControl extends Control {

	/**
	 * Normal value range maximum for any of the Control.value. Used for scaling, e.g.
	 * in bar graphs.
	 */
	public Float maxValue;
	/**
	 * Normal value range minimum for any of the Control.value. Used for scaling, e.g.
	 * in bar graphs.
	 */
	public Float minValue;

	public AnalogControl(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}