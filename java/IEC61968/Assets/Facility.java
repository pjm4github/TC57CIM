package IEC61968.Assets;

import IEC61970.Base.Domain.String;

/**
 * A facility may contain buildings, storage facilities, switching facilities,
 * power generation, manufacturing facilities, maintenance facilities, etc.
 * @created 07-Jan-2024 9:47:10 PM
 */
public class Facility extends AssetContainer {

	/**
	 * Kind of this facility.
	 */
	public String kind;

	public Facility(){

	}
}//end Facility