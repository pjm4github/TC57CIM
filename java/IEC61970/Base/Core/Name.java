package TC57CIM.IEC61970.Base.Core;

import TC57CIM.IEC61970.Base.Domain.String;

/**
 * The Name class provides the means to define any number of human readable  names
 * for an object. A name is <b>not</b> to be used for defining inter-object
 * relationships. For inter-object relationships instead use the object
 * identification 'mRID'.
 * @author T. Kostic
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public class Name {

	/**
	 * Any free text that name the object.
	 */
	public String name;
	/**
	 * Type of this name.
	 */
	public NameType NameType;
	/**
	 * Identified object that this name designates.
	 */
	public IdentifiedObject IdentifiedObject;

	public Name(){

	}

	public void finalize() throws Throwable {

	}

}