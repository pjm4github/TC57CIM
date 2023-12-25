package TC57CIM.IEC61970.Base.ICCPConfiguration;

import TC57CIM.IEC61970.Base.Domain.String;
import TC57CIM.IEC61970.Base.SCADA.CommunicationLink;

/**
 * @author SELAOST1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class IPAccessPoint extends CommunicationLink {

	public String address;
	public IPAddressKind addressType;
	public String gateway;
	public String subnet;

	public IPAccessPoint(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}