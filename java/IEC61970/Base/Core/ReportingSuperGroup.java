package IEC61970.Base.Core;


/**
 * A reporting super group, groups reporting groups for a higher level report.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class ReportingSuperGroup extends IdentifiedObject {

	/**
	 * Reporting groups that are grouped under this super group.
	 */
	public ReportingGroup ReportingGroup;

	public ReportingSuperGroup(){

	}
}//end ReportingSuperGroup