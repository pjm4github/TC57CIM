package IEC62325.MarketManagement;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Decimal;

/**
 * An identification of a set of values beeing adressed within a specific interval
 * of time.
 * @author effantin-cyr
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class Point {

	/**
	 * A sequential value representing the relative position within a given time
	 * interval.
	 */
	public Integer position;
	/**
	 * The quality of the information being provided. This quality may be estimated,
	 * not available, as provided, etc.
	 */
	public String quality;
	/**
	 * Principal quantity identified for a point.
	 */
	public Decimal quantity;
	/**
	 * Secondary quantity identified for a point.
	 */
	public Decimal secondaryQuantity;
	public Period Period;
	public TimeSeries TimeSeries;
	public AceTariffType AceTariffType;

	public Point(){

	}
}//end Point