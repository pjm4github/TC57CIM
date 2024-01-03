package IEC61968.InfIEC61968.InfAssets;

import IEC61970.Base.Domain.Temperature;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Voltage;
import IEC61968.Common.Status;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61970.Base.Wires.TransformerTank;

/**
 * Common information captured during transformer inspections and/or diagnostics.
 * Note that some properties may be measured through other means and therefore
 * have measurement values in addition to the observed values recorded here.
 * @created 03-Jan-2024 12:28:05 PM
 */
public class TransformerObservation extends IdentifiedObject {

	/**
	 * Bushing temperature.
	 */
	public Temperature bushingTemp;
	/**
	 * Dissolved Gas Analysis. Typical values are: Acceptable, Overheating, Corona,
	 * Sparking, Arcing.
	 */
	public String dga;
	/**
	 * Frequency Response Analysis. Typical values are: acceptable, slight movement,
	 * significant movement, failed, near failure. A graphic of the response diagram,
	 * which is a type of document, may be associated with this analysis through the
	 * recursive document relationship of the ProcedureDataSet.
	 */
	public String freqResp;
	/**
	 * Overall measure of furfural in oil and mechanical strength of paper. DP, the
	 * degree of polymerization, is the strength of the paper. Furfural is a measure
	 * of furfural compounds, often expressed in parts per million.
	 */
	public String furfuralDP;
	/**
	 * Hotspot oil temperature.
	 */
	public Temperature hotSpotTemp;
	/**
	 * Oil Quality Analysis-Color.
	 */
	public String oilColor;
	/**
	 * Oil Quality Analysis-Dielectric Strength.
	 */
	public Voltage oilDielectricStrength;
	/**
	 * Oil Quality Analysis- inter facial tension (IFT) - number-Dynes/CM.
	 */
	public String oilIFT;
	/**
	 * The level of oil in the transformer.
	 */
	public String oilLevel;
	/**
	 * Oil Quality Analysis-Neutralization Number - Number - Mg KOH.
	 */
	public String oilNeutralizationNumber;
	/**
	 * Pump vibration, with typical values being: nominal, high.
	 */
	public String pumpVibration;
	public Status status;
	/**
	 * Top oil temperature.
	 */
	public Temperature topOilTemp;
	/**
	 * Water Content expressed in parts per million.
	 */
	public String waterContent;
	public WindingInsulation WindingInsulationPFs;
	public TransformerTank Transformer;

	public TransformerObservation(){

	}
}//end TransformerObservation