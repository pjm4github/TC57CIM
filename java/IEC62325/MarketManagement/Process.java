package IEC62325.MarketManagement;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * The formal specification of a set of business transactions having the same
 * business goal.
 * @created 03-Jan-2024 1:58:51 PM
 */
public class Process extends IdentifiedObject {

	/**
	 * The classification mechanism used to group a set of objects together within a
	 * business process. The grouping may be of a detailed or a summary nature.
	 */
	public String classificationType;
	/**
	 * The kind of business process.
	 */
	public String processType;
	public MarketDocument MarketDocument;

	public Process(){

	}
}//end Process