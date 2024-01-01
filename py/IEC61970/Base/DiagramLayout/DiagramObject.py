
from typing import Optional

from IEC61970.Base.DiagramLayout.Diagram import Diagram
from IEC61970.Base.DiagramLayout.DiagramObjectPoint import DiagramObjectPoint
from IEC61970.Base.DiagramLayout.DiagramObjectStyle import DiagramObjectStyle
from IEC61970.Base.DiagramLayout.VisibilityLayer import VisibilityLayer
from IEC61970.Base.Domain.AngleDegrees import AngleDegrees


class DiagramObject:
    """
    An object that defines one or more points in a given space. This object can be associated with anything that
    specializes IdentifiedObject. For single line diagrams such objects typically include such items as analog values,
    breakers, disconnectors, power transformers, and transmission lines.
    """

    def __init__(self) -> None:
        self.drawing_orderOptional[int] = 0  # The drawing order of this element
        self.is_polygonOptional[bool] = True    # Defines whether or not the diagram objects points define the boundaries of a polygon
        self.offset_xOptional[float] = 1.0      # The offset in the X direction
        self.offset_yOptional[float] = 1.0      # The offset in the Y direction
        self.rotationOptional[AngleDegrees] = AngleDegrees()   # Sets the angle of rotation of the diagram object
        self.diagramOptional[Diagram] = Diagram()      # A diagram object is part of a diagram
        self.visibility_layersOptional[VisibilityLayer] = VisibilityLayer()   # A diagram object can be part of multiple visibility layers
        self.diagram_object_pointsOptional[DiagramObjectPoint] = DiagramObjectPoint()   # A diagram object can have 0 or more points to reflect its layout position
        self.diagram_object_styleOptional[DiagramObjectStyle] = DiagramObjectStyle()   # A diagram object has a style associated that provides a reference for the style used in the originating system

