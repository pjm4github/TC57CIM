from uuid import uuid4

class IdentifiedObject:
    """This is a root class to provide common identification for all classes needing
    identification and naming attributes.
    """
    # The diagram objects that are associated with the domain object.


    def __init__(self, uuid=None, alias_name=None, description=None, name=None):
        self.mRID = str(uuid4()) if uuid is None else uuid
        self.alias_name = alias_name
        self.description = description
        self.name = name
        # self.diagram_objects= DiagramObject()