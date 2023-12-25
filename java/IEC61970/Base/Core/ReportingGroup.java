package TC57CIM.IEC61970.Base.Core;


/**
 * A reporting group is used for various ad-hoc groupings used for reporting.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:29 PM
 */
public class ReportingGroup extends IdentifiedObject {

	/**
	 * Power system resources which belong to this reporting group.
	 */
	public PowerSystemResource PowerSystemResource;

	public ReportingGroup(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}