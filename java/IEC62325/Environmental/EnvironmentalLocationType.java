package IEC62325.Environmental;

import IEC62325.Environmental.EnvDomain.LocationKind;
import IEC61968.Common.Location;

/**
 * Type of environmental location. Used when an environmental alert or phenomenon
 * has multiple locations associated with it.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class EnvironmentalLocationType {

	/**
	 * The kind of location. Typical values might be center, extent, primary,
	 * secondary, etc. 
	 */
	public LocationKind kind;
	/**
	 * Location of this instance of ths kind of environmental location. 
	 */
	public Location Location;

	public EnvironmentalLocationType(){

	}
}//end EnvironmentalLocationType