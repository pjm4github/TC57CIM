package IEC61970.Base.ICCPConfiguration;

import IEC61970.Base.Domain.String;
import IEC61970.Base.SCADA.CommunicationLink;

/**
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class IPAccessPoint extends CommunicationLink {

	public String address;
	public IPAddressKind addressType;
	public String gateway;
	public String subnet;

	public IPAccessPoint(){

	}
}//end IPAccessPoint