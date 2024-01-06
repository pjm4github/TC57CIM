# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:55:15 2024
# class NetworkBoundary
from IEC61970.InfIEC61970.InfPart303.NetworkModelFrames.FrameworkPart import FrameworkPart
from IEC61970.InfIEC61970.InfPart303.NetworkModelFrames.NetworkFrame import NetworkFrame


class NetworkBoundary(FrameworkPart):
    """
    A framework part that is a boundary between 2 frames.
    @author 222206
    @version 1.0
    @created 25-Dec-2023 8:32:00 PM
    """
    
    # public attribute m_network_frame
    def __init__(self):
        super().__init__()
        self.m_network_frame = NetworkFrame()  # Initialize m_network_frame as a NetworkFrame object.
