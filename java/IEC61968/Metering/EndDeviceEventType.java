package IEC61968.Metering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Detailed description for an event produced by an end device. Values in
 * attributes allow for creation of recommended codes to be used for identifying
 * end device events as follows: <type>.<domain>.<subDomain>.<eventOrAction>.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:21 PM
 */
public class EndDeviceEventType extends IdentifiedObject {

	/**
	 * High-level nature of the event. By properly classifying events by a small set
	 * of domain codes, a system can more easily run reports based on the types of
	 * events that have occurred or been received.
	 */
	public String domain;
	/**
	 * The most specific part of this event type. It is mainly in the form of a verb
	 * that gives action to the event that just occurred.
	 */
	public String eventOrAction;
	/**
	 * More specific nature of the event, as a further sub-categorisation of 'domain'.
	 */
	public String subDomain;
	/**
	 * Type of physical device from which the event was created. A value of zero (0)
	 * can be used when the source is unknown.
	 */
	public String type;

	public EndDeviceEventType(){

	}
}//end EndDeviceEventType