package IEC61970.Base.Generation.Production;

import IEC61970.Base.Core.Curve;

/**
 * Accounts for tracking emissions usage and credits for thermal generating units.
 * A unit may have zero or more emission accounts, and will typically have one for
 * tracking usage and one for tracking credits.
 * @created 02-Jan-2024 10:52:49 PM
 */
public class EmissionAccount extends Curve {

	/**
	 * The type of emission, for example sulfur dioxide (SO2). The y1AxisUnits of the
	 * curve contains the unit of measure (e.g. kg) and the emissionType is the type
	 * of emission (e.g. sulfer dioxide).
	 */
	public EmissionType emissionType;
	/**
	 * The source of the emission value.
	 */
	public EmissionValueSource emissionValueSource;

	public EmissionAccount(){

	}
}//end EmissionAccount