# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106


class ResourceDeploymentStatus:
    """
    @author mspivbe2
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        # Comments to explain why the acceptance status. For example, to explain why a
        # request is accepted only partially, instead of fully.
        self.accept_comments = ""

        # Status of the resource for this deployment. Values include (full compliance,
        # partial compliance, opt-out, etc.)
        self.accept_status = ""

        # The MW amount the resource can contribute for this deployment. This is from the
        # DR provider - as a response? Or actual? Does this belong in settlement? Discuss
        # more.
        self.resource_response_mw = 0.0
