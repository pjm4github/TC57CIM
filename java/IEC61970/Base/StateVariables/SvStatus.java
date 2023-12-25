package TC57CIM.IEC61970.Base.StateVariables;

import TC57CIM.IEC61970.Base.Domain.Boolean;
import TC57CIM.IEC61970.Base.Wires.SinglePhaseKind;
import TC57CIM.IEC61970.Base.Core.ConductingEquipment;

/**
 * State variable for status.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:29 PM
 */
public class SvStatus extends StateVariable {

	/**
	 * The in service status as a result of topology processing.
	 */
	public Boolean inService;
	/**
	 * The individual phase status.    If the attribute is unspecified, then three
	 * phase model is assumed.
	 */
	public SinglePhaseKind phase;
	/**
	 * The conducting equipment associated with the status state variable.
	 */
	public ConductingEquipment ConductingEquipment;

	public SvStatus(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}