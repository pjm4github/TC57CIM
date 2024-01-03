package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Integer;

/**
 * IDC (Interchange Distribution Calulator) sends data for a TLR (Transmission
 * Loading Relief).
 * @created 28-Dec-2023 12:13:19 PM
 */
public class FlowgateRelief {

	/**
	 * Date/Time when record becomes effective
	 * Used to determine when a record becomes effective.
	 */
	public DateTime effectiveDate;
	/**
	 * Energy Flow level that should be maintained according to the TLR rules as
	 * specified by the IDC.
	 * For Realtime Markets use in dispatch to control constraints under TLR and
	 * calculate unconstrained market flows
	 */
	public Integer idcTargetMktFlow;
	/**
	 * Date/Time when record is no longer effective
	 * Used to determine when a record is no longer effective
	 */
	public DateTime terminateDate;

	public FlowgateRelief(){

	}
}//end FlowgateRelief