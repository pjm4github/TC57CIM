package IEC61968.Assets;

import IEC61970.Base.Domain.Temperature;

/**
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class OilSpecimen extends Specimen {

	public OilSampleLocation oilSampleTakenFrom;
	public Temperature oilSampleTemperature;
	public OilTemperatureSource oilTemperatureSource;
	public SampleContainerType sampleContainer;

	public OilSpecimen(){

	}
}//end OilSpecimen