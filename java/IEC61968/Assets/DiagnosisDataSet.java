package IEC61968.Assets;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.PhaseCode;
import IEC61970.Base.Domain.DateTime;

/**
 * The result of a problem (typically an asset failure) diagnosis. Contains
 * complete information like what might be received from a lab doing forensic
 * analysis of a failed asset.
 * @created 07-Jan-2024 9:46:30 PM
 */
public class DiagnosisDataSet extends ProcedureDataSet {

	/**
	 * Effect of problem.
	 */
	public String effect;
	/**
	 * Failuer mode, for example: Failure to Insulate; Failure to conduct; Failure to
	 * contain oil; Failure to provide ground plane; Other.
	 */
	public String failureMode;
	/**
	 * Cause of problem determined during diagnosis.
	 */
	public String finalCause;
	/**
	 * Code for diagnosed probem type.
	 */
	public String finalCode;
	/**
	 * Origin of problem determined during diagnosis.
	 */
	public String finalOrigin;
	/**
	 * Remarks pertaining to findings during problem diagnosis.
	 */
	public String finalRemark;
	/**
	 * Phase(s) diagnosed.
	 */
	public PhaseCode phaseCode;
	/**
	 * Code for problem type determined during preliminary assessment.
	 */
	public String preliminaryCode;
	/**
	 * Date and time preliminary assessment of problem was performed.
	 */
	public DateTime preliminaryDateTime;
	/**
	 * Remarks pertaining to preliminary assessment of problem.
	 */
	public String preliminaryRemark;
	/**
	 * Root cause of problem determined during diagnosis.
	 */
	public String rootCause;
	/**
	 * Root origin of problem determined during diagnosis.
	 */
	public String rootOrigin;
	/**
	 * Remarks pertaining to root cause findings during problem diagnosis.
	 */
	public String rootRemark;

	public DiagnosisDataSet(){

	}
}//end DiagnosisDataSet