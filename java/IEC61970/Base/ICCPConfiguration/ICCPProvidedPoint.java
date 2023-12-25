package TC57CIM.IEC61970.Base.ICCPConfiguration;


/**
 * The IdentifiedObject.name attribute must have a value.  The name attribute
 * shall be used as the DataValue name used for the exchange.
 * @author SELAOST1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class ICCPProvidedPoint extends ProvidedBilateralPoint {

	/**
	 * Provides information regarding the access privileges allowed to the ICCP Point.
	 */
	public ICCPAccessPrivilegeKind accessPriviledge;
	/**
	 * Specifies the type of ICCP quality that will be conveyed as part of the ICCP
	 * Point.
	 */
	public ICCPQualityKind pointQuality;
	/**
	 * Indicates the ICCP Point type that is to be conveyed.
	 * 
	 * A CIM AccumlatorValue  shall be mapped to an ICCP real.
	 * A CIM AnalogValue shall be mapped to an ICCP real.
	 * A CIM DiscreteValue shall be mapped to either an ICCP real, state,
	 * stateSupplemental, or either protection event type.
	 * A CIM StringMeasurementValue does not have a standardized mapping.
	 */
	public ICCPPointKind pointType;
	public ICCPScope scope;

	public ICCPProvidedPoint(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}