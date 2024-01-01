# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:50:27 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Core.Terminal import Terminal
from IEC61970.Dynamics.StandardInterconnections.RemoteSignalKind import RemoteSignalKind


class RemoteInputSignal(IdentifiedObject):
    """
    Supports connection to a terminal associated with a remote bus from which an
    input signal of a specific type is coming.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 10:55:49 PM
    """

    def __init__(self) -> None:
        """
        Constructor for initializing the RemoteInputSignal object.
        """
        super().__init__()
        self.remote_signal_type: RemoteSignalKind = RemoteSignalKind.REMOTE_BUS_VOLTAGE
        self.terminal: Terminal = Terminal()  # remote terminal
