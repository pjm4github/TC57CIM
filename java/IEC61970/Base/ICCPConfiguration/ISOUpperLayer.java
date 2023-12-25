package TC57CIM.IEC61970.Base.ICCPConfiguration;

import TC57CIM.IEC61970.Base.Domain.Integer;
import TC57CIM.IEC61970.Base.Domain.String;

/**
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class ISOUpperLayer extends TCPAccessPoint {

	public Integer aeInvoke;
	/**
	 * Is the AE qualifier and represents further application level addressing
	 * information.
	 */
	public Integer aeQual;
	/**
	 * Is a further application level OSI addressing parameter.
	 */
	public Integer apInvoke;
	/**
	 * Is a sequence of integer strings separated by ".".  The value, in conjunction
	 * with other application addressing attributes (e.g. other APs) are used to
	 * select a specific application (e.g. the ICCP application entity) per the OSI
	 * reference model.  The sequence, and its values, represent a namespace whose
	 * values are governed by ISO/IEC 7498-3.
	 */
	public String apTitle;
	/**
	 * Is the addressing selector for OSI presentation addressing.
	 */
	public String osiPsel;
	/**
	 * Is the OSI session layer addressing information.
	 */
	public String osiSsel;
	/**
	 * Is the OSI Transport Layer addressing information.
	 */
	public String osiTsel;

	public ISOUpperLayer(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}