package IEC61970.Base.ICCPConfiguration;

import IEC61970.Base.Domain.Integer;

/**
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class TCPAccessPoint extends IPAccessPoint {

	public Integer keepAliveTime;
	/**
	 * This value is only needed to be specified for called nodes (e.g. those that
	 * respond to a TCP.Open request).
	 * 
	 * This value specifies the TCP port to be used. Well known and "registered" ports
	 * are preferred and can be found at:
	 * http://www.iana.org/assignments/service-names-port-numbers/service-names-port-
	 * numbers.xhtml
	 * 
	 * For IEC 60870-6 TASE.2 (e.g. ICCP) and IEC 61850, the value used shall be 102
	 * for non-TLS protected exchanges. The value shall be 3782 for TLS transported
	 * ICCP and 61850 exchanges.
	 */
	public Integer port;

	public TCPAccessPoint(){

	}
}//end TCPAccessPoint