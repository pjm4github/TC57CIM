package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Boolean;
import IEC62325.InfIEC62325.InfEnergyScheduling.TransmissionCorridor;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * An electrical connection, link, or line consisting of one or more parallel
 * transmission elements between two areas of the interconnected electric systems,
 * or portions thereof. TransmissionCorridor and TransmissionRightOfWay refer to
 * legal aspects. The TransmissionPath refers to the segments between a
 * TransmissionProvider's ServicePoints.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class TransmissionPath extends IdentifiedObject {

	/**
	 * The available transmission capability of a transmission path for the reference
	 * direction.
	 */
	public ActivePower availTransferCapability;
	/**
	 * Flag which indicates if the transmission path is also a designated
	 * interconnection "parallel path".
	 */
	public Boolean parallelPathFlag;
	/**
	 * The total transmission capability of a transmission path in the reference
	 * direction.
	 */
	public ActivePower totalTransferCapability;
	/**
	 * A TransmissionPath is contained in a TransmissionCorridor.
	 */
	public TransmissionCorridor For;
	public TransmissionReservation TransmissionReservation;

	public TransmissionPath(){

	}
}//end TransmissionPath