package IEC61970.Base.Meas;

import IEC61970.Base.Domain.Float;

/**
 * An analog control used for supervisory control.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
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
}//end AnalogControl