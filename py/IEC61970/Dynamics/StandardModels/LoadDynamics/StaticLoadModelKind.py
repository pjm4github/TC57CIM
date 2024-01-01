# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 16:32:51 2023
from enum import Enum


class StaticLoadModelKind(Enum):
    """
    Type of static load model.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    # Exponential P and Q equations are used and the following attributes are required:
    # kp1, kp2, kp3, kpf, ep1, ep2, ep3
    # kq1, kq2, kq3, kqf, eq1, eq2, eq3.
    EXPONENTIAL = 1

    # ZIP1 P and Q equations are used and the following attributes are required:
    # kp1, kp2, kp3, kpf
    # kq1, kq2, kq3, kqf.
    ZIP1 = 2

    # This model separates the frequency-dependent load (primarily motors) from other
    # load. ZIP2 P and Q equations are used and the following attributes are required:
    # kp1, kp2, kp3, kq4, kpf
    # kq1, kq2, kq3, kq4, kqf.
    ZIP2 = 3

    # The load is represented as a constant impedance. ConstantZ P and Q equations
    # are used and no attributes are required.
    CONSTANT_Z = 4
