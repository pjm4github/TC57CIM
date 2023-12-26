package IEC61968.Assets;

import IEC61970.Base.Domain.Temperature;
import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Sample or specimen of a material (fluid or solid).
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class Specimen extends IdentifiedObject {

	/**
	 * Operating ambient temperature (in øC).
	 */
	public Temperature ambientTemperatureAtSampling;
	/**
	 * Operating ambient humidity (in percent).
	 */
	public PerCent humidityAtSampling;
	/**
	 * Identifier of specimen used in inspection or test.
	 */
	public String specimenID;
	/**
	 * Date and time sample specimen taken.
	 */
	public DateTime specimenSampleDateTime;
	/**
	 * Date and time the specimen was received by the lab.
	 */
	public DateTime specimenToLabDateTime;
	/**
	 * Test sampler taker who gathered this specimen.
	 */
	public AssetTestSampleTaker AssetTestSampleTaker;

	public Specimen(){

	}
}//end Specimen