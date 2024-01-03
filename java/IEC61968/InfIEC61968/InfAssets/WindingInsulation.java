package IEC61968.InfIEC61968.InfAssets;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Reactance;
import IEC61968.Common.Status;
import IEC61970.Base.Wires.TransformerEnd;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Winding insulation condition as a result of a test.
 * @created 29-Dec-2023 6:10:04 PM
 */
public class WindingInsulation extends IdentifiedObject {

	/**
	 * Status of Winding Insulation Power Factor as of statusDate: Acceptable, Minor
	 * Deterioration or Moisture Absorption, Major Deterioration or Moisture
	 * Absorption, Failed.
	 */
	public String insulationPFStatus;
	/**
	 * For testType, status of Winding Insulation Resistance as of statusDate. Typical
	 * values are: Acceptable, Questionable, Failed.
	 */
	public String insulationResistance;
	/**
	 * As of statusDate, the leakage reactance measured at the "from" winding with the
	 * "to" winding short-circuited and all other windings open-circuited.
	 */
	public Reactance leakageReactance;
	public Status status;
	public TransformerEnd ToWinding;
	public TransformerEnd FromWinding;

	public WindingInsulation(){

	}
}//end WindingInsulation