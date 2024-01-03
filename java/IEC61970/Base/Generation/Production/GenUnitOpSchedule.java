package IEC61970.Base.Generation.Production;

import IEC61970.Base.Core.RegularIntervalSchedule;

/**
 * The generating unit's Operator-approved current operating schedule (or plan),
 * typically produced with the aid of unit commitment type analyses. The X-axis
 * represents absolute time. The Y1-axis represents the status (0=off-line and
 * unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.).
 * The Y2-axis represents the must run fixed power value where required.
 * @created 02-Jan-2024 10:53:49 PM
 */
public class GenUnitOpSchedule extends RegularIntervalSchedule {

	public GenUnitOpSchedule(){

	}
}//end GenUnitOpSchedule