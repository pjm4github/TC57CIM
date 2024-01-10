# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.Seconds import Seconds


class ExcSt4B:
    """Modified IEEE ST4B static excitation system with maximum inner loop feedback
    gain Vgmax.
    @author: tsaxton
    @version: 1.0
    @created: 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        """Constructor"""
        self.kc: float = 0.1  # Rectifier loading factor proportional to commutating reactance (Kc). Typical Value =
        # 0.113
        self.kg: float = 0.0  # Feedback gain constant of the inner loop field regulator (Kg). Typical Value = 0
        self.ki: float = 0.0  # Potential circuit gain coefficient (Ki). Typical Value = 0
        self.kim: float = 0.0  # Voltage regulator integral gain output (Kim). Typical Value = 0
        self.kir: float = 10.75  # Voltage regulator integral gain (Kir). Typical Value = 10.75
        self.kp: float = 9.3  # Potential circuit gain coefficient (Kp). Typical Value = 9.3
        self.kpm: float = 1.0  # Voltage regulator proportional gain output (Kpm). Typical Value = 1
        self.kpr: float = 10.75  # Voltage regulator proportional gain (Kpr). Typical Value = 10.75
        self.lvgate: bool = False  # Selector (LVgate). true = LVgate is part of the block diagram. false = LVgate is
        # not part of the block diagram. Typical Value = False
        self.ta: Seconds = Seconds(0.02)  # Voltage regulator time constant (Ta). Typical Value = 0.02
        self.thetap: float = 0.0  # Potential circuit phase angle (thetap). Typical Value = 0
        self.uel: bool = False  # Selector (Uel). true = UEL is part of block diagram. false = UEL is not part of
        # block diagram. Typical Value = False
        self.vbmax: float = 11.63  # Maximum excitation voltage (Vbmax). Typical Value = 11.63
        self.vgmax: float = 5.8  # Maximum inner loop feedback voltage (Vgmax). Typical Value = 5.8
        self.vmmax: float = 99.0  # Maximum inner loop output (Vmmax). Typical Value = 99
        self.vmmin: float = -99.0  # Minimum inner loop output (Vmmin). Typical Value = -99
        self.vrmax: float = 1.0  # Maximum voltage regulator output (Vrmax). Typical Value = 1
        self.vrmin: float = -0.87  # Minimum voltage regulator output (Vrmin). Typical Value = -0.87
        self.xl: float = 0.124  # Reactance associated with potential source (Xl). Typical Value = 0.124
