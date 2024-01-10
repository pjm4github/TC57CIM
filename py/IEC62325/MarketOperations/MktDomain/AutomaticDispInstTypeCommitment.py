from enum import Enum


class AutomaticDispInstTypeCommitment(Enum):
    """
    Commitment instruction types.
    @created 28-Dec-2023 3:05:54 PM
    """

    # 	 * Start up instruction type
    START_UP = 1

    # 	 * Shut down instruction type
    SHUT_DOWN = 2

    # 	 * Distributed Resource Deployment
    DR_DEPLOY = 3

    # 	 * Distributed Resource Release
    DR_RELEASE = 4

    # 	 * Distributed Resource adjustment for a distributed resource that is already
    # 	 * deployed (committed).
    DR_ADJUSTMENT = 5
