package IEC61968.Common;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.StringQuantity;
import IEC61968.InfIEC61968.InfAssets.Specification;
import IEC61968.Assets.ProcedureDataSet;
import IEC61968.PaymentMetering.Transaction;

/**
 * Generic name-value pair class, with optional sequence number and units for
 * value; can be used to model parts of information exchange when concrete types
 * are not known in advance.
 * @created 25-Dec-2023 8:45:25 PM
 */
public class UserAttribute {

	/**
	 * Name of an attribute.
	 */
	public String name;
	/**
	 * Sequence number for this attribute in a list of attributes.
	 */
	public Integer sequenceNumber;
	/**
	 * Value of an attribute, including unit information.
	 */
	public StringQuantity value;
	public Specification RatingSpecification;
	public Specification PropertySpecification;
	public ProcedureDataSet ProcedureDataSets;
	/**
	 * Transaction for which this snapshot has been recorded.
	 */
	public Transaction Transaction;

	public UserAttribute(){

	}
}//end UserAttribute