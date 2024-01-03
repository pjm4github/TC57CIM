package IEC62325.InfIEC62325.InfReservation;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.MarketOpCommon.MktMeasurement;

/**
 * Site of an interface between interchange areas. The tie point can be a network
 * branch (e.g., transmission line or transformer) or a switching device. For
 * transmission lines, the interchange area boundary is usually at a designated
 * point such as the middle of the line. Line end metering is then corrected for
 * line losses.
 * @created 03-Jan-2024 1:55:05 PM
 */
public class TiePoint extends IdentifiedObject {

	/**
	 * The MW rating of the tie point.
	 */
	public ActivePower tiePointMWRating;
	/**
	 * A measurement is made on the A side of a tie point
	 */
	public MktMeasurement ForMktMeasurement;
	/**
	 * A measurement is made on the B side of a tie point
	 */
	public MktMeasurement ByMktMeasurement;

	public TiePoint(){

	}
}//end TiePoint