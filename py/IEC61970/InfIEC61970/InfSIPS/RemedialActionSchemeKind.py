from enum import Enum


class RemedialActionSchemeKind(Enum):
    """
    Classification of Remedial Action Scheme.
    Author: sveinols
    Version: 1.0
    Created: 02-Jan-2024 9:37:07 PM
    """
    RAS = 1  # "rAS"  # Remedial Action Scheme (RAS).
    RAP = 2  # "rAP"  # Remedial Action Plan (RAP)
