# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:41:50 2023
from IEC61968.InfIEC61968.InfAssetInfo.RegulationBranchKind import RegulationBranchKind
from IEC61968.InfIEC61968.InfAssetInfo.ShuntImpedanceControlKind import ShuntImpedanceControlKind
from IEC61968.InfIEC61968.InfAssetInfo.ShuntImpedanceLocalControlKind import ShuntImpedanceLocalControlKind
from IEC61970.Base.Core.PhaseCode import PhaseCode
from IEC61970.Base.Domain.Hours import Hours
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.ReactivePower import ReactivePower
from IEC61970.Base.Wires.RegulatingControl import RegulatingControl


class ShuntCompensatorControl(RegulatingControl):
    """
    Distribution capacitor bank control settings.
    @created 29-Dec-2023 5:59:54 PM
    """

    def __init__(self):
        super().__init__()

        # For VAR, amp, or power factor locally controlled shunt impedances, the flow direction: in, out.
        self.branch_direct = 0

        # The size of the individual units that make up the bank.
        self.cell_size = ReactivePower()

        # Kind of control (if any).
        self.control_kind = ShuntImpedanceControlKind.REMOTE_WITH_LOCAL_OVERRIDE

        # For locally controlled shunt impedances which have a voltage override feature,
        # the high voltage override value. If the voltage is above this value, the shunt
        # impedance will be turned off regardless of the other local controller settings.
        self.high_voltage_override = PU()

        # Kind of local controller.
        self.local_control_kind = ShuntImpedanceLocalControlKind.VOLTAGE

        # Upper control setting.
        self.local_off_level = ""

        # Lower control setting.
        self.local_on_level = ""

        # True if the locally controlled capacitor has voltage override capability.
        self.local_override = False

        # For locally controlled shunt impedances which have a voltage override feature,
        # the low voltage override value. If the voltage is below this value, the shunt
        # impedance will be turned on regardless of the other local controller settings.
        self.low_voltage_override = PU()

        # IdmsShuntImpedanceData.maxNumSwitchOps.
        self.max_switch_operation_count = 0

        # True if open is normal status for a fixed capacitor bank, otherwise normal
        # status is closed.
        self.normal_open = False

        # For VAR, amp, or power factor locally controlled shunt impedances, the index of
        # the regulation branch.
        self.reg_branch = ""

        # For VAR, amp, or power factor locally controlled shunt impedances, the end of
        # the branch that is regulated. The field has the following values: from side, to
        # side, and tertiary (only if the branch is a transformer).
        self.reg_branch_end = 0

        # (For VAR, amp, or power factor locally controlled shunt impedances) Kind of
        # regulation branch.
        self.reg_branch_kind = RegulationBranchKind.SWITCH

        # Phases that are measured for controlling the device.
        self.sensing_phase_code = PhaseCode()

        # Time interval between consecutive switching operations.
        self.switch_operation_cycle = Hours()

        # True if regulated voltages are measured line to line, otherwise they are
        # measured line to ground.
        self.v_reg_line_line = False
