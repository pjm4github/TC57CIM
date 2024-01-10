# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class PssIeee4B(PowerSystemStabilizerDynamics):

    def __init__(self) -> None:
        super().__init__()
        self.bwh1: float = 0.0  # Notch filter 1 (high-frequency band): Three dB bandwidth (B<sub>wi</sub>).
        self.bwh2: float = 0.0  # Notch filter 2 (high-frequency band): Three dB bandwidth (B<sub>wi</sub>).

        self.bwl1: float = 0.0  # Notch filter 1 (low-frequency band): Three dB bandwidth (B<sub>wi</sub>).

        self.bwl2: float = 0.0  # Notch filter 2 (low-frequency band): Three dB bandwidth (B<sub>wi</sub>).

        self.kh: PU = PU(120)  # High band gain (K<sub>H</sub>).  Typical Value = 120.
        self.kh1: PU = PU(66)  # High band differential filter gain (K<sub>H1</sub>).  Typical Value = 66.
        self.kh11: PU = PU(1)  # High band first lead-lag blocks coefficient (K<sub>H11</sub>).  Typical Value = 1.
        self.kh17: PU = PU(1)  # High band first lead-lag blocks coefficient (K<sub>H17</sub>).  Typical Value = 1.
        self.kh2: PU = PU(66)  # High band differential filter gain (K<sub>H2</sub>).  Typical Value = 66.
        self.ki: PU = PU(30)  # Intermediate band gain (K<sub>I</sub>).  Typical Value = 30.
        self.ki1: PU = PU(66)  # Intermediate band differential filter gain (K<sub>I1</sub>).  Typical Value = 66.
        self.ki11: PU = PU(
            1)  # Intermediate band first lead-lag blocks coefficient (K<sub>I11</sub>).  Typical Value = 1.
        self.ki17: PU = PU(
            1)  # Intermediate band first lead-lag blocks coefficient (K<sub>I17</sub>).  Typical Value = 1.
        self.ki2: PU = PU(66)  # Intermediate band differential filter gain (K<sub>I2</sub>).  Typical Value = 66.
        self.kl: PU = PU(7.5)  # Low band gain (K<sub>L</sub>).  Typical Value = 7.5.
        self.kl1: PU = PU(66)  # Low band differential filter gain (K<sub>L1</sub>).  Typical Value = 66.
        self.kl11: PU = PU(1)  # Low band first lead-lag blocks coefficient (K<sub>L11</sub>).  Typical Value = 1.
        self.kl17: PU = PU(1)  # Low band first lead-lag blocks coefficient (K<sub>L17</sub>).  Typical Value = 1.
        self.kl2: PU = PU(66)  # Low band differential filter gain (K<sub>L2</sub>).  Typical Value = 66.
        self.omeganh1: float = 0.0  # Notch filter 1 (high-frequency band): filter frequency (omega<sub>ni</sub>).

        self.omeganh2: float = 0.0  # Notch filter 2 (high-frequency band): filter frequency (omega<sub>ni</sub>).

        self.omeganl1: float = 0.0  # Notch filter 1 (low-frequency band): filter frequency (omega<sub>ni</sub>).

        self.omeganl2: float = 0.0  # Notch filter 2 (low-frequency band): filter frequency (omega<sub>ni</sub>).

        self.th1: Seconds = Seconds(0.1513)  # High band time constant (T<sub>H1</sub>).  Typical Value = 0.01513.
        self.th10: Seconds = Seconds(0)  # High band time constant (T<sub>H10</sub>).  Typical Value = 0.
        self.th11: Seconds = Seconds(0)  # High band time constant (T<sub>H11</sub>).  Typical Value = 0.
        self.th12: Seconds = Seconds(0)  # High band time constant (T<sub>H12</sub>).  Typical Value = 0.
        self.th2: Seconds = Seconds(0.01816)  # High band time constant (T<sub>H2</sub>).  Typical Value = 0.01816.
        self.th3: Seconds = Seconds(0)  # High band time constant (T<sub>H3</sub>).  Typical Value = 0.
        self.th4: Seconds = Seconds(0)  # High band time constant (T<sub>H4</sub>).  Typical Value = 0.
        self.th5: Seconds = Seconds(0)  # High band time constant (T<sub>H5</sub>).  Typical Value = 0.
        self.th6: Seconds = Seconds(0)  # High band time constant (T<sub>H6</sub>).  Typical Value = 0.
        self.th7: Seconds = Seconds(0.01816)  # High band time constant (T<sub>H7</sub>).  Typical Value = 0.01816.
        self.th8: Seconds = Seconds(0.02179)  # High band time constant (T<sub>H8</sub>).  Typical Value = 0.02179.
        self.th9: Seconds = Seconds(0)  # High band time constant (T<sub>H9</sub>).  Typical Value = 0.
        self.ti1: Seconds = Seconds(.173)  # Intermediate band time constant (T<sub>I1</sub>).  Typical Value = 0.173.
        self.ti10: Seconds = Seconds(0)  # Intermediate band time constant (T<sub>I11</sub>).  Typical Value = 0.
        self.ti11: Seconds = Seconds(0)  # Intermediate band time constant (T<sub>I11</sub>).  Typical Value = 0.
        self.ti12: Seconds = Seconds(0)  # Intermediate band time constant (T<sub>I2</sub>).  Typical Value = 0.
        self.ti2: Seconds = Seconds(.2075)  # Intermediate band time constant (T<sub>I2</sub>).  Typical Value = 0.2075.
        self.ti3: Seconds = Seconds(0)  # Intermediate band time constant (T<sub>I3</sub>).  Typical Value = 0.
        self.ti4: Seconds = Seconds(0)  # Intermediate band time constant (T<sub>I4</sub>).  Typical Value = 0.
        self.ti5: Seconds = Seconds(0)  # Intermediate band time constant (T<sub>I5</sub>).  Typical Value = 0.
        self.ti6: Seconds = Seconds(0)  # Intermediate band time constant (T<sub>I6</sub>).  Typical Value = 0.
        self.ti7: Seconds = Seconds(.2075)  # Intermediate band time constant (T<sub>I7</sub>).  Typical Value = 0.2075.
        self.ti8: Seconds = Seconds(.2491)  # Intermediate band time constant (T<sub>I8</sub>).  Typical Value = 0.2491.
        self.ti9: Seconds = Seconds(0)  # Intermediate band time constant (T<sub>I9</sub>).  Typical Value = 0.
        self.tl1: Seconds = Seconds(1.73)  # Low band time constant (T<sub>L1</sub>).  Typical Value = 1.73.
        self.tl10: Seconds = Seconds(0)  # Low band time constant (T<sub>L10</sub>).  Typical Value = 0.
        self.tl11: Seconds = Seconds(0)  # Low band time constant (T<sub>L11</sub>).  Typical Value = 0.
        self.tl12: Seconds = Seconds(0)  # Low band time constant (T<sub>L12</sub>).  Typical Value = 0.
        self.tl2: Seconds = Seconds(2.075)  # Low band time constant (T<sub>L2</sub>).  Typical Value = 2.075.
        self.tl3: Seconds = Seconds(0)  # Low band time constant (T<sub>L3</sub>).  Typical Value = 0.
        self.tl4: Seconds = Seconds(0)  # Low band time constant (T<sub>L4</sub>).  Typical Value = 0.
        self.tl5: Seconds = Seconds(0)  # Low band time constant (T<sub>L5</sub>).  Typical Value = 0.
        self.tl6: Seconds = Seconds(0)  # Low band time constant (T<sub>L6</sub>).  Typical Value = 0.
        self.tl7: Seconds = Seconds(2.075)  # Low band time constant (T<sub>L7</sub>).  Typical Value = 2.075.
        self.tl8: Seconds = Seconds(2.491)  # Low band time constant (T<sub>L8</sub>).  Typical Value = 2.491.
        self.tl9: Seconds = Seconds(0)  # Low band time constant (T<sub>L9</sub>).  Typical Value = 0.
        self.vhmax: PU = PU(.6)  # High band output maximum limit (V<sub>Hmax</sub>).  Typical Value = 0.6.
        self.vhmin: PU = PU(-.6)  # High band output minimum limit (V<sub>Hmin</sub>).  Typical Value = -0.6.
        self.vimax: PU = PU(.6)  # Intermediate band output maximum limit (V<sub>Imax</sub>).  Typical Value = 0.6.
        self.vimin: PU = PU(-.6)  # Intermediate band output minimum limit (V<sub>Imin</sub>).  Typical Value = -0.6.
        self.vlmax: PU = PU(.075)  # Low band output maximum limit (V<sub>Lmax</sub>).  Typical Value = 0.075.
        self.vlmin: PU = PU(-.075)  # Low band output minimum limit (V<sub>Lmin</sub>).  Typical Value = -0.075.
        self.vstmax: PU = PU(.15)  # PSS output maximum limit (V<sub>STmax</sub>).  Typical Value = 0.15.
        self.vstmin: PU = PU(-.15)  # PSS output minimum limit (V<sub>STmin</sub>).  Typical Value = -0.15.
