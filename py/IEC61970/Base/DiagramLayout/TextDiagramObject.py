# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:25:23 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DiagramLayout.DiagramObject import DiagramObject


class TextDiagramObject(DiagramObject):
    """
    A diagram object for placing free-text or text derived from an associated domain object.
    @author mcmorran
    @version 1.0
    @created 15-Dec-2023 4:38:30 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.text: str = ""
