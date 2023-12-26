package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.ReferenceData.Flowgate;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Generic constraints can represent secure areas, voltage profile, transient
 * stability and voltage collapse limits.
 * 
 * The generic constraints can be one of the following forms:
 * a)	Thermal MW limit constraints type
 * b)	Group line flow constraint type
 * @author USRAKHA
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class GenericConstraints extends IdentifiedObject {

	/**
	 * Interval End Time
	 */
	public DateTime intervalEndTime;
	/**
	 * Interval Start Time
	 */
	public DateTime intervalStartTime;
	/**
	 * Maximum Limit (MW)
	 */
	public Float maxLimit;
	/**
	 * Minimum Limit (MW)
	 */
	public Float minLimit;
	public Flowgate Flowgate;
	public TransmissionCapacity TransmissionCapacity;

	public GenericConstraints(){

	}
}//end GenericConstraints