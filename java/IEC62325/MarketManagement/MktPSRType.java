package IEC62325.MarketManagement;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.PSRType;

/**
 * The type of a power system resource.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class MktPSRType extends PSRType {

	/**
	 * The coded type of a power system resource.
	 */
	public String psrType;
	public TimeSeries TimeSeries;

	public MktPSRType(){

	}
}//end MktPSRType