package IEC61970.Base.ICCPConfiguration;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.String;

/**
 * This contains the information that a particular actor exposes for a particular
 * agreed upon ICCP Bilateral Table.
 * @author herb
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class ICCPVirtualControlCenter extends BilateralExchangeActor {

	public IEC62351-6ApplicationSecurityKind applicationSecurityRequirement;
	/**
	 * Used to indicate if the Provider is responsible for initiating the TASE.2
	 * connection.  If the value is TRUE, the provider is responsible for establishing
	 * the association.  If the value is FALSE, the peer provider of the Bilateral
	 * Table will need to establish the association.
	 */
	public Boolean calling;
	/**
	 * If True the value indicates that the entity represented by the bilateral table
	 * is capable of issuing requests and responding to request (e.g. bidirectional
	 * support of ICCP requests).
	 * 
	 * If False, this indicates that a calling entity (e.g. calling = True) will not
	 * be able to respond to ICCP requests.  If False, and calling=False, this
	 * indicates that the entity will only respond to ICCP requests and not issue ICCP
	 * requests.
	 */
	public Boolean clientAndServer;
	/**
	 * Specifies the fastest update interval that can be provided for integrity
	 * information and Transfer Set creation. The value is in seconds.
	 */
	public Integer minimumUpdateInterval;
	/**
	 * Specifies the ICC scope name that the remote can use to access the information
	 * in the Bilateral Table if the information is not VCC scoped.  This value may
	 * not be null.
	 */
	public String nameOfLocalICC;
	/**
	 * Per IEC 60870-6-702:  If true indicates support for basic services.  Must
	 * always be true.
	 */
	public Boolean supportForBlock1;
	/**
	 * Per IEC 60870-6-702:  If true indicates support for extended conditions.
	 */
	public Boolean supportForBlock2;
	/**
	 * Per IEC 60870-6-702:  If true indicates support for blocked transfers. 
	 */
	public Boolean supportForBlock3;
	/**
	 * Per IEC 60870-6-702:  If true indicates support for information messages. 
	 */
	public Boolean supportForBlock4;
	/**
	 * Per IEC 60870-6-702:  If true indicates support for device control. 
	 */
	public Boolean supportForBlock5;
	/**
	 * Per IEC 60870-6-702:  If true indicates support for accounts.  The use of this
	 * block was deprecated in Edition 3.
	 */
	public Boolean supportForDepriciatedBlock8;
	/**
	 * If true, then transport level security as specified by IEC 62351-6 is required.
	 */
	public Boolean TransportSecurityRequirement;

	public ICCPVirtualControlCenter(){

	}
}//end ICCPVirtualControlCenter