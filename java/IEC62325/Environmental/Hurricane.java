package IEC62325.Environmental;

import IEC61970.Base.Domain.Integer;

/**
 * A hurricane, a subtype of cyclone occurring in the North Atlantic Ocean or
 * North-eastern Pacific Ocean whose intensity is measured using the Saffir-
 * Simpson Hurricane Scale.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class Hurricane extends Cyclone {

	/**
	 * The hurricane's category during the time interval, using Saffir-Simpson
	 * Hurricane Wind Scale, a 1 to 5 rating based on a hurricane's sustained wind
	 * speed.
	 */
	public Integer category;

	public Hurricane(){

	}
}//end Hurricane