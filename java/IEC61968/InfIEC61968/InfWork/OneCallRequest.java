package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;

/**
 * A request for other utilities to mark their underground facilities prior to
 * commencement of construction and/or maintenance.
 * @created 03-Jan-2024 12:58:56 PM
 */
public class OneCallRequest extends WorkDocument {

	/**
	 * True if explosives have been or are planned to be used.
	 */
	public Boolean explosivesUsed;
	/**
	 * True if work location has been marked, for example for a dig area.
	 */
	public Boolean markedIndicator;
	/**
	 * Instructions for marking a dig area, if applicable.
	 */
	public String markingInstruction;

	public OneCallRequest(){

	}
}//end OneCallRequest