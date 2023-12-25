package TC57CIM.IEC61970.Base.ControlArea;

import TC57CIM.IEC61970.Base.Generation.Production.GeneratingUnit;
import TC57CIM.IEC61970.Base.Core.IdentifiedObject;

/**
 * A control area generating unit. This class is needed so that alternate control
 * area definitions may include the same generating unit.   Note only one instance
 * within a control area should reference a specific generating unit.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class ControlAreaGeneratingUnit extends IdentifiedObject {

	/**
	 * The generating unit specified for this control area.  Note that a control area
	 * should include a GeneratingUnit only once.
	 */
	public GeneratingUnit GeneratingUnit;
	/**
	 * The link to prioritized measurements for this GeneratingUnit.
	 */
	public AltGeneratingUnitMeas AltGeneratingUnitMeas;

	public ControlAreaGeneratingUnit(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}