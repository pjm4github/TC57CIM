# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:03:56 2023
#
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class ACDCTerminal(IdentifiedObject):
    """
    An electrical connection point (AC or DC) to a piece of conducting equipment.
    Terminals are connected at physical connection points called connectivity nodes.
    """

    def __init__(self) -> None:
        super().__init__()
        self.connected: bool = False
        """
        The connected status is related to a bus-branch model and the topological node
        to terminal relation. True implies the terminal is connected to the related
        topological node and false implies it is not.
        """

        self.sequence_number: int = 0
        """
        The orientation of the terminal connections for a multiple terminal conducting
        equipment. The sequence numbering starts with 1 and additional terminals
        should follow in increasing order. The first terminal is the "starting point"
        for a two terminal branch.
        """
