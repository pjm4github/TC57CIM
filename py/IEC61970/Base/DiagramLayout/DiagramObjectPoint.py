# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:25:23 2023
from typing import Optional
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DiagramLayout.DiagramObjectGluePoint import DiagramObjectGluePoint


class DiagramObjectPoint:
    """
    A point in a given space defined by three coordinates and associated to a diagram
    object.  The coordinates may be positive or negative as the origin does not
    have to be in the corner of a diagram.
    """
    def __init__(self) -> None:
        self.sequence_number: Optional[int] = 0  # The sequence position of the point
        self.x_position: Optional[float] = 0.0  # The X coordinate of this point
        self.y_position: Optional[float] = 0.0  # The Y coordinate of this point
        self.z_position: Optional[float] = 0.0  # The Z coordinate of this point
        self.diagram_object_glue_point: Optional[DiagramObjectGluePoint] = DiagramObjectGluePoint()  # The 'glue' point to which this point is associated
