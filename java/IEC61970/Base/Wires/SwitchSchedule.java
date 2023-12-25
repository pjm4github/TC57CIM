package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.LoadModel.SeasonDayTypeSchedule;

/**
 * A schedule of switch positions.  If RegularTimePoint.value1 is 0, the switch is
 * open.  If 1, the switch is closed.
 * @author KLH
 * @version 1.0
 * @created 15-Dec-2023 4:38:29 PM
 */
public class SwitchSchedule extends SeasonDayTypeSchedule {

	public SwitchSchedule(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}