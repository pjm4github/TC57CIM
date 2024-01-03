package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * The defined termination points of a transmission path. Service points are
 * defined from the viewpoint of the transmission service. Each service point is
 * contained within (or on the boundary of) an interchange area. A service point
 * is source or destination of a transaction.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class ServicePoint extends IdentifiedObject {

	/**
	 * A transmission path has a "point-of-receipt" service point
	 */
	public TransmissionPath PORTransmissionPath;
	/**
	 * A transmission path has a "point-of-delivery" service point
	 */
	public TransmissionPath PODTransmissionPath;
	public TransmissionReservation SourceReservation;
	public TransmissionReservation SinkReservation;

	public ServicePoint(){

	}
}//end ServicePoint