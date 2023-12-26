package IEC62325.Environmental;

import IEC62325.Environmental.EnvDomain.FScale;
import IEC61970.Base.Domain.Length;

/**
 * A tornado, a violent destructive whirling wind accompanied by a funnel-shaped
 * cloud that progresses in a narrow path over the land.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class Tornado extends AtmosphericPhenomenon {

	/**
	 * Fujita scale (referred to as EF-scale starting in 2007) for the tornado.
	 */
	public FScale fScale;
	/**
	 * Width of the tornado during the time interval.
	 */
	public Length width;

	public Tornado(){

	}
}//end Tornado