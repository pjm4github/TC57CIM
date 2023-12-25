# from phase_code import PhaseCode
# from connectivity_node import ConnectivityNode
# from conducting_equipment import ConductingEquipment
# from regulating_control import RegulatingControl
# from ac_dc_terminal import ACDCTerminal
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ACDCTerminal import ACDCTerminal
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ConductingEquipment import ConductingEquipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ConnectivityNode import ConnectivityNode
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.PhaseCode import PhaseCode
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RegulatingControl import RegulatingControl


class Terminal(ACDCTerminal):
    """
    An AC electrical connection point to a piece of conducting equipment. Terminals
    are connected at physical connection points called connectivity nodes.
    """
    def __init__(self):
        super().__init__()
        self.phases = PhaseCode()  # Represents the normal network phasing condition. If the attribute is missing, three phases (ABC or ABCN) shall be assumed.
        self.connectivity_node = ConnectivityNode()  # The connectivity node to which this terminal connects with zero impedance.
        self.conducting_equipment = ConductingEquipment()  # The conducting equipment of the terminal. Conducting equipment have terminals that may be connected to other conducting equipment terminals via connectivity nodes or topological nodes.
        self.regulating_control = RegulatingControl()  # The controls regulating this terminal.
