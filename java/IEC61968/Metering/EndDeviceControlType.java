package IEC61968.Metering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Detailed description for a control produced by an end device. Values in
 * attributes allow for creation of recommended codes to be used for identifying
 * end device controls as follows: <type>.<domain>.<subDomain>.<eventOrAction>.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:21 PM
 */
public class EndDeviceControlType extends IdentifiedObject {

	/**
	 * High-level nature of the control.
	 */
	public String domain;
	/**
	 * The most specific part of this control type. It is mainly in the form of a verb
	 * that gives action to the control that just occurred.
	 */
	public String eventOrAction;
	/**
	 * More specific nature of the control, as a further sub-categorisation of
	 * 'domain'.
	 */
	public String subDomain;
	/**
	 * Type of physical device from which the control was created. A value of zero (0)
	 * can be used when the source is unknown.
	 */
	public String type;

	public EndDeviceControlType(){

	}
}//end EndDeviceControlType