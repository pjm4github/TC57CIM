package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Input pin for a logical gate. The condition described in the input pin will
 * give a logical true or false. Result from measurement and calculation are
 * converted to a true or false.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:31:26 PM
 */
public class GateInputPin extends IdentifiedObject {

	/**
	 * If true, use the absolute value for compare.. 
	 */
	public Boolean absoluteValue;
	/**
	 * The compare operation.
	 */
	public AnalogToDigitalLogicKind aDLogicKind;
	/**
	 * The duration the compare condition need to be present before given a true.
	 * Default is 0 seconds.
	 */
	public Seconds duration;
	/**
	 * Invert/negate the result of the compare.
	 */
	public Boolean negate;
	/**
	 * The threshold percentage that should be used for compare with the percentage
	 * change between input value and threshold value.
	 */
	public PerCent thresholdPercentage;
	/**
	 * The threshold value that should be used for compare with the input value.
	 */
	public Float thresholdValue;

	public GateInputPin(){

	}
}//end GateInputPin