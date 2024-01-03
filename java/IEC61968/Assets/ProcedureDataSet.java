package IEC61968.Assets;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Meas.MeasurementValue;
import IEC61968.InfIEC61968.InfAssets.TransformerObservation;
import IEC61968.Work.WorkTask;
import IEC61968.Common.Document;

/**
 * A data set recorded each time a procedure is executed. Observed results are
 * captured in associated measurement values and/or values for properties relevant
 * to the type of procedure performed.
 * @created 03-Jan-2024 12:06:14 PM
 */
public class ProcedureDataSet extends Document {

	/**
	 * Date and time procedure was completed.
	 */
	public DateTime completedDateTime;
	/**
	 * Asset to which this procedure data set applies.
	 */
	public Asset Asset;
	public MeasurementValue MeasurementValue;
	public TransformerObservation TransformerObservations;
	/**
	 * Work task that created this procedure data set.
	 */
	public WorkTask WorkTask;

	public ProcedureDataSet(){

	}
}//end ProcedureDataSet