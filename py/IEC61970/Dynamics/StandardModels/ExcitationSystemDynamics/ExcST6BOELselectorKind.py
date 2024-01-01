"""java
package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

/**
 * Type of connection for the OEL input used for static excitation systems type 6B.
 *
 * @author civanov
 * @version 1.0
 * @created 29-Dec-2023 11:24:18 PM
 */
public enum ExcST6BOELselectorKind {
}
"""

# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from enum import Enum


class ExcST6BOELselectorKind(Enum):
    # /**
    #  * No OEL input is used.
    #  */
    # NO_OEL_INPUT,
    NO_OEL_INPUT = 1
    #
    # /**
    #  * The connection is before UEL.
    #  */
    # BEFORE_UEL,
    BEFORE_UEL = 2
    #
    # /**
    #  * The connection is after UEL.
    #  */
    # AFTER_UEL
    AFTER_UEL = 3

