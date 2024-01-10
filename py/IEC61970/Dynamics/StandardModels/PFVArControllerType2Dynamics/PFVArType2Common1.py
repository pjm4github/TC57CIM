# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:02:30 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Dynamics.StandardModels.PFVArControllerType2Dynamics.PFVArControllerType2Dynamics import \
    PFVArControllerType2Dynamics


class PfVarType2Common1(PFVArControllerType2Dynamics):
    """
    Power factor / Reactive power regulator. This model represents the power factor
    or reactive power controller such as the Basler SCP-250. The controller
    measures power factor or reactive power (PU on generator rated power) and
    compares it with the operator's set point.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.j: bool = True  # Selector (J). True = control mode for reactive power, False = control mode for power factor.
        self.ki: PU = PU()  # Reset gain (Ki).
        self.kp: PU = PU()  # Proportional gain (Kp).
        self.max: PU = PU()  # Output limit (max).
        self.ref: PU = PU()  # Reference value of reactive power or power factor (Ref).
