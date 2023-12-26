package IEC61968.Work;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;

/**
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class InternalLocation extends WorkLocation {

	public String buildingName;
	public String buildingNumber;
	public Integer floor;
	public String roomNumber;

	public InternalLocation(){

	}
}//end InternalLocation