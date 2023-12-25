# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# ami_billing_ready_kind.py

from enum import Enum

class AmiBillingReadyKind(Enum):
    # Usage point is equipped with an AMI capable meter having communications capability.
    ENABLED = 1

    # Usage point is equipped with an AMI capable meter that is functioning and communicating with the AMI network.
    OPERABLE = 2

    # Usage point is equipped with an operating AMI capable meter and accuracy has been certified for billing purposes.
    BILLING_APPROVED = 3

    # Usage point is equipped with a non AMI capable meter.
    NON_AMI = 4

    # Usage point is equipped with an AMI capable meter; however, the AMI functionality has been disabled or is not being used.
    AMI_DISABLED = 5

    # USAGE point is equipped with an AMI capable meter that is not yet currently equipped with a communications module.
    AMI_CAPABLE = 6

    # Usage point is not currently equipped with a meter.
    NON_METERED = 7
