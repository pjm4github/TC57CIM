from enum import Enum


class GateLogicKind(Enum):
    """
    Created on:      17-Dec-2023 3:54:04 PM
    Original author: sveinols
    """
    AND = 1  # A logical AND operation. True when all input are true.
    OR = 2  # A logical OR operation. True when one or more input are true.
    NOR = 3  # A logical NOR operation. False when one or more input are true.
    NAND = 4  # A logical NAND operation. False when all input are true.
    NOT = 5  # A logical NOT operation. Only one input and true input will give false out and
    # false in will give true out. An inverter.
    XNOR = 6  # A logical XNOR operation. The function is the inverse of the exclusive OR (XOR)
    # gate. All input false or true will give true, otherwise false.
    XOR = 7  # A logical XOR operation.  All input false or true will give false, otherwise true.
