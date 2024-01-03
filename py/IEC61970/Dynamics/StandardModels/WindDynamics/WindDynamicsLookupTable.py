# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from typing import Optional
from enum import Enum

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Dynamics.StandardModels.WindDynamics.WindContCurrLimIEC import WindContCurrLimIEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindContPType3IEC import WindContPType3IEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindContQPQULimIEC import WindContQPQULimIEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindContRotorRIEC import WindContRotorRIEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindGenType3bIEC import WindGenType3bIEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindLookupTableFunctionKind import WindLookupTableFunctionKind
from IEC61970.Dynamics.StandardModels.WindDynamics.WindPitchContPowerIEC import WindPitchContPowerIEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindPlantFreqPcontrolIEC import WindPlantFreqPcontrolIEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindPlantReactiveControlIEC import WindPlantReactiveControlIEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindProtectionIEC import WindProtectionIEC


class WindDynamicsLookupTable(IdentifiedObject):
    """
    The class models a look up table for the purpose of wind standard models.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    def __init__(self) -> None:
        # Input value (x) for the lookup table function.
        super().__init__()
        self.input: float = 1.0

        # Type of the lookup table function.
        self.lookup_table_function_type: Optional[WindLookupTableFunctionKind] = WindLookupTableFunctionKind.OMEGA_P

        # Output value (y) for the lookup table function.
        self.output: float = 1.0

        # Sequence numbers of the pairs of the input (x) and the output (y) of the lookup table function.
        self.sequence: Optional[int] = None

        # The frequency and active power wind plant control model with which this wind    dynamics lookup table is associated.
        self.wind_plant_freq_pcontrol_iec: Optional[WindPlantFreqPcontrolIEC] = WindPlantFreqPcontrolIEC()

        # The voltage and reactive power wind plant control model with which this wind dynamics lookup table is associated.
        self.wind_plant_reactive_control_iec: Optional[WindPlantReactiveControlIEC] = WindPlantReactiveControlIEC()

        # The grid protection model with which this wind dynamics lookup table is associated.
        self.wind_protection_iec: Optional[WindProtectionIEC] = WindProtectionIEC()

        # The QP and QU limitation model with which this wind dynamics lookup table is associated.
        self.wind_cont_qpqu_lim_iec: Optional[WindContQPQULimIEC] = WindContQPQULimIEC()

        # The current control limitation model with which this wind dynamics lookup table  is associated.
        self.wind_cont_curr_lim_iec: Optional[WindContCurrLimIEC] = WindContCurrLimIEC()

        # The P control type 3 model with which this wind dynamics lookup table isassociated.
        self.wind_cont_ptype3_iec: Optional[WindContPType3IEC] = WindContPType3IEC()

        # The rotor resistance control model with which this wind dynamics lookup table is associated.
        self.wind_cont_rotor_riec: Optional[WindContRotorRIEC] = WindContRotorRIEC()

        # The pitch control power model with which this wind dynamics lookup table is  associated.
        self.wind_pitch_cont_power_iec: Optional[WindPitchContPowerIEC] = WindPitchContPowerIEC()

        # The generator type 3B model with which this wind dynamics lookup table is  associated.
        self.wind_gen_type3b_iec: Optional[WindGenType3bIEC] = WindGenType3bIEC()
