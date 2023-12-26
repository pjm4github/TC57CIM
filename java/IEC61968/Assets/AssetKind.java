package IEC61968.Assets;


/**
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public enum AssetKind {
	breakerAirBlastBreaker,
	breakerBulkOilBreaker,
	breakerMinimumOilBreaker,
	breakerSF6DeadTankBreaker,
	breakerSF6LiveTankBreaker,
	breakerTankAssembly,
	breakerInsulatingStackAssembly,
	transformer,
	transformerTank,
	/**
	 * Other type of Asset. The type attribute may provide more details in this case.
	 */
	other
}