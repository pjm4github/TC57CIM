# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:25:23 2023
from typing import Optional

class VisibilityLayer:
    """
    Layers are typically used for grouping diagram objects according to themes and
    scales. Themes are used to display or hide certain information (e.g., lakes,
    borders), while scales are used for hiding or displaying information depending
    on the current zoom level (hide text when it is too small to be read, or when
    it exceeds the screen size). This is also called de-cluttering.
    
    CIM based graphics exchange will support an m:n relationship between diagram
    objects and layers. It will be the task of the importing system to convert an
    m:n case into an appropriate 1:n representation if the importing system does not
    support m:n.
    
    @author mcmorran
    @version 1.0
    @created 15-Dec-2023 4:38:30 PM
    """

    def __init__(self) -> None:
        self.drawing_order: Optional[int] = 0

