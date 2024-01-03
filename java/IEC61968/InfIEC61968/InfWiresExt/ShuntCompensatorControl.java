package IEC61968.InfIEC61968.InfWiresExt;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.ReactivePower;
import IEC61968.InfIEC61968.InfAssetInfo.ShuntImpedanceControlKind;
import IEC61970.Base.Domain.PU;
import IEC61968.InfIEC61968.InfAssetInfo.ShuntImpedanceLocalControlKind;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Boolean;
import IEC61968.InfIEC61968.InfAssetInfo.RegulationBranchKind;
import IEC61970.Base.Core.PhaseCode;
import IEC61970.Base.Domain.Hours;
import IEC61970.Base.Wires.RegulatingControl;

/**
 * Distribution capacitor bank control settings.
 * @created 29-Dec-2023 5:59:54 PM
 */
public class ShuntCompensatorControl extends RegulatingControl {

	/**
	 * For VAR, amp, or power factor locally controlled shunt impedances, the flow
	 * direction: in, out.
	 */
	public Integer branchDirect;
	/**
	 * The size of the individual units that make up the bank.
	 */
	public ReactivePower cellSize;
	/**
	 * Kind of control (if any).
	 */
	public ShuntImpedanceControlKind controlKind;
	/**
	 * For locally controlled shunt impedances which have a voltage override feature,
	 * the high voltage override value. If the voltage is above this value, the shunt
	 * impedance will be turned off regardless of the other local controller settings.
	 */
	public PU highVoltageOverride;
	/**
	 * Kind of local controller.
	 */
	public ShuntImpedanceLocalControlKind localControlKind;
	/**
	 * Upper control setting.
	 */
	public String localOffLevel;
	/**
	 * Lower control setting.
	 */
	public String localOnLevel;
	/**
	 * True if the locally controlled capacitor has voltage override capability.
	 */
	public Boolean localOverride;
	/**
	 * For locally controlled shunt impedances which have a voltage override feature,
	 * the low voltage override value. If the voltage is below this value, the shunt
	 * impedance will be turned on regardless of the other local controller settings.
	 */
	public PU lowVoltageOverride;
	/**
	 * IdmsShuntImpedanceData.maxNumSwitchOps.
	 */
	public Integer maxSwitchOperationCount;
	/**
	 * True if open is normal status for a fixed capacitor bank, otherwise normal
	 * status is closed.
	 */
	public Boolean normalOpen;
	/**
	 * For VAR, amp, or power factor locally controlled shunt impedances, the index of
	 * the regulation branch.
	 */
	public String regBranch;
	/**
	 * For VAR, amp, or power factor locally controlled shunt impedances, the end of
	 * the branch that is regulated. The field has the following values: from side, to
	 * side, and tertiary (only if the branch is a transformer).
	 */
	public Integer regBranchEnd;
	/**
	 * (For VAR, amp, or power factor locally controlled shunt impedances) Kind of
	 * regulation branch.
	 */
	public RegulationBranchKind regBranchKind;
	/**
	 * Phases that are measured for controlling the device.
	 */
	public PhaseCode sensingPhaseCode;
	/**
	 * Time interval between consecutive switching operations.
	 */
	public Hours switchOperationCycle;
	/**
	 * True if regulated voltages are measured line to line, otherwise they are
	 * measured line to ground.
	 */
	public Boolean vRegLineLine;

	public ShuntCompensatorControl(){

	}
}//end ShuntCompensatorControl