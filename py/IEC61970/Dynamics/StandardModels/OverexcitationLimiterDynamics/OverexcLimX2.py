# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:00:52 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds


class OverexcLimX2:
    """
        Field Voltage or Current overexcitation limiter designed to protect the
    generator field of an AC machine with automatic excitation control from
    overheating due to prolonged overexcitation.
    """

    def __init__(self) -> None:
        # 	 * Low voltage or current point on the inverse time characteristic
        # 	 * (EFD<sub>1</sub>).  Typical Value = 1.1.
        self.efd1: PU = PU(1.1)  # Low voltage or current point on the inverse time characteristic (EFD1). Typical Value = 1.1.

        # 	 * Mid voltage or current point on the inverse time characteristic
        # 	 * (EFD<sub>2</sub>).  Typical Value = 1.2.
        self.efd2: PU = PU(1.2) # Mid voltage or current point on the inverse time characteristic (EFD2). Typical Value = 1.2.

        # 	 * High voltage or current point on the inverse time characteristic
        # 	 * (EFD<sub>3</sub>).  Typical Value = 1.5.
        self.efd3: PU = PU(1.5)  # High voltage or current point on the inverse time characteristic (EFD3). Typical Value = 1.5.
        # 	 * Desired field voltage if m=F or field current if m=T (EFD<sub>DES</sub>).
        # 	 * Typical Value = 1.
        self.efddes: PU = PU(1.0)  # Desired field voltage if m=F or field current if m=T (EFDDES). Typical Value = 1.0.
        # 	 * Rated field voltage if m=F or field current if m=T (EFD<sub>RATED</sub>).
        # 	 * Typical Value = 1.05.
        self.efdrated: PU = PU(1.0) # Rated field voltage if m=F or field current if m=T (EFDRATED). Typical Value = 1.05.

        # 	 * Gain (K<sub>MX</sub>).  Typical Value = 0.002.
        self.kmx: PU = PU(0.002)  # Gain (KMX). Typical Value = 0.002.

        # 	 * true = IFD limiting
        # 	 * false = EFD limiting.
        self.m: bool = False  # m: true = IFD limiting, false = EFD limiting.
        # 	public Boolean m;
        # 	 * Time to trip the exciter at the low voltage or current point on the inverse
        # 	 * time characteristic (TIME<sub>1</sub>).  Typical Value = 120.
        self.t1: Seconds = Seconds(120)  # Time to trip the exciter at the low voltage or current point on the inverse time characteristic (TIME1). Typical Value = 120.

        # 	public Seconds t1;
        # 	 * Time to trip the exciter at the mid voltage or current point on the inverse
        # 	 * time characteristic (TIME<sub>2</sub>).  Typical Value = 40.
        self.t2: Seconds = Seconds(40) # Time to trip the exciter at the mid voltage or current point on the inverse time characteristic (TIME2). Typical Value = 40.

        # 	public Seconds t2;
        # 	 * Time to trip the exciter at the high voltage or current point on the inverse
        # 	 * time characteristic (TIME<sub>3</sub>).  Typical Value = 15.
        self.t3: Seconds = Seconds(15)  # Time to trip the exciter at the high voltage or current point on the inverse time characteristic (TIME3). Typical Value = 15.
        # 	public Seconds t3;
        # 	 * Low voltage limit (V<sub>LOW</sub>) (>0).
        # 	public PU vlow;
        self.vlow: PU = PU(0.1)  # Low voltage limit (VLOW) (>0).

