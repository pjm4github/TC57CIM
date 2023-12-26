package IEC62325.MarketManagement;

import IEC61970.Base.Domain.String;

/**
 * The motivation of an act.
 * @author effantin-cyr
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class Reason {

	/**
	 * The motivation of an act in coded form.
	 */
	public String code;
	/**
	 * The textual explanation corresponding to the reason code.
	 */
	public String text;
	public MarketDocument MarketDocument;
	public Point Point;

	public Reason(){

	}
}//end Reason