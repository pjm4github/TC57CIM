package IEC61968.InfIEC61968.InfAssets;

import IEC61968.Common.Status;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Bushing insulation power factor condition as a result of a test.
 * Typical status values are: Acceptable, Minor Deterioration or Moisture
 * Absorption, Major Deterioration or Moisture Absorption, Failed.
 * @created 03-Jan-2024 12:25:35 PM
 */
public class BushingInsulationPF extends IdentifiedObject {

	public Status status;
	/**
	 * Kind of test for this bushing.
	 */
	public BushingInsulationPfTestKind testKind;
	public TransformerObservation TransformerObservation;

	public BushingInsulationPF(){

	}
}//end BushingInsulationPF