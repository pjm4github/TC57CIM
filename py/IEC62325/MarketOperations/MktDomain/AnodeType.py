from enum import Enum


class AnodeType(Enum):
    """
    Aggregated Nodes Types for example:
     - SYS - System Zone/Region; </li>
     - RUC - RUC Zone; </li>
     - LFZ - Load Forecast Zone; </li>
     - REG - Market Energy/Ancillary Service Region; </li>
     - AGR - Aggregate Generation Resource; </li>
     - POD - Point of Delivery; </li>
     - ALR - Aggregate Load Resource; </li>
     - LTAC - Load TransmissionAccessCharge (TAC) Group;</li>
     - ACA - Adjacent Control Area</li>
     - ASR - Aggregated System Resource</li>
     - ECA - Embedded Control Area</li>

     @created 28-Dec-2023 3:05:27 PM
     """

    # System Zone/Region;
    SYS = 1
    # RUC Zone
    RUC = 2
    # Load Forecast Zone
    LFZ = 3
    # Market Energy/Ancillary Service Region;
    REG = 4
    # Aggregate Generation Resource;
    AGR = 5
    # Point of Delivery;
    POD = 6
    # Aggregate Load Resource;
    ALR = 7
    # Load TransmissionAccessCharge (TAC) Group;
    LTAC = 8
    # Adjacent Control Area
    ACA = 9
    # Aggregated System Resource
    ASR = 10
    # Embedded Control Area
    ECA = 11
    # Distributed Energy Resource.
    DER = 12
