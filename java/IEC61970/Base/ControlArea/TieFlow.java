package TC57CIM.IEC61970.Base.ControlArea;

import TC57CIM.IEC61970.Base.Domain.Boolean;
import TC57CIM.IEC61970.Base.Core.Terminal;
import TC57CIM.IEC61970.Base.Core.IdentifiedObject;

/**
 * A flow specification in terms of location and direction for a control area.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:30 PM
 */
public class TieFlow extends IdentifiedObject {

	/**
	 * True if the flow into the terminal (load convention) is also flow into the
	 * control area.  For example, this attribute should be true if using the tie line
	 * terminal further away from the control area. For example to represent a tie to
	 * a shunt component (like a load or generator) in another area, this is the near
	 * end of a branch and this attribute would be specified as false.
	 */
	public Boolean positiveFlowIn;
	/**
	 * The terminal to which this tie flow belongs.
	 */
	public Terminal Terminal;
	/**
	 * The primary and alternate tie flow measurements associated with the tie flow.
	 */
	public AltTieMeas AltTieMeas;

	public TieFlow(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}