package IEC61968.Assets;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Meas.Measurement;
import IEC61970.Base.Meas.Limit;
import IEC61968.Common.Document;

/**
 * Documented procedure for various types of work or work tasks on assets.
 * @created 07-Jan-2024 9:48:37 PM
 */
public class Procedure extends Document {

	/**
	 * Textual description of this procedure.
	 */
	public String instruction;
	/**
	 * Kind of procedure.
	 */
	public ProcedureKind kind;
	/**
	 * Sequence number in a sequence of procedures being performed.
	 */
	public String sequenceNumber;
	/**
	 * Document containing this measurement.
	 */
	public Measurement Measurements;
	public Limit Limits;
	/**
	 * All assets to which this procedure applies.
	 */
	public Asset Assets;
	/**
	 * All data sets captured by this procedure.
	 */
	public ProcedureDataSet ProcedureDataSets;

	public Procedure(){

	}
}//end Procedure