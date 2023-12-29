# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 12:50:20 2023


from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class InternalControlArea(IdentifiedObject):
    """
    There is one internal control area in the system, which is the single control
    area in the primary network company. Real time generation control affects only
    the internal control area.
    @created 27-Dec-2023 12:44:35 PM
    """
    def __init__(self) -> None:
        super().__init__()
