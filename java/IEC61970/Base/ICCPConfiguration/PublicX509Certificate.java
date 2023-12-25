package TC57CIM.IEC61970.Base.ICCPConfiguration;

import TC57CIM.IEC61970.Base.Domain.String;

/**
 * Used to convey information that will allow matching in order to determine which
 * certificate to use.  Actual certificates are exchanged externally to the CIM
 * exchange.
 * @author herb
 * @version 1.0
 * @created 15-Dec-2023 4:38:29 PM
 */
public class PublicX509Certificate {

	/**
	 * Represents the CA that issued the certificate.  Defined to be per X.509.
	 */
	public String issuerName;
	/**
	 * Is the serial number of the certificate per X.509 definition.
	 */
	public String serialNumber;
	public TCPAccessPoint TCPAccessPoint;
	public ISOUpperLayer ISOUpperLayer;

	public PublicX509Certificate(){

	}

	public void finalize() throws Throwable {

	}

}