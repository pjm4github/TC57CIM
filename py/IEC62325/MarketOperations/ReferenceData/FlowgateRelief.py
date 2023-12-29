# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC61970.Base.Domain.DateTime import DateTime


class FlowgateRelief:
    """
    IDC (Interchange Distribution Calulator) sends data for a TLR (Transmission
    Loading Relief).
    @created 28-Dec-2023 12:13:19 PM
    """
    def __init__(self) -> None:
        # 	/**
        # 	 * Date/Time when record becomes effective
        # 	 * Used to determine when a record becomes effective.
        # 	 */
        self.effective_date: DateTime = DateTime()
        # 	 * Energy Flow level that should be maintained according to the TLR rules as
        # 	 * specified by the IDC.
        # 	 * For Realtime Markets use in dispatch to control constraints under TLR and
        # 	 * calculate unconstrained market flows
        self.idc_target_mkt_flow: int = 0
        # 	 * Date/Time when record is no longer effective
        # 	 * Used to determine when a record is no longer effective
        self.terminate_date: DateTime = DateTime()
