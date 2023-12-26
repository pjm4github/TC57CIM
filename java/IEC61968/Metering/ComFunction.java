package IEC61968.Metering;

import IEC61970.Base.Domain.String;

/**
 * Communication function of communication equipment or a device such as a meter.
 * @created 25-Dec-2023 8:45:20 PM
 */
public class ComFunction extends EndDeviceFunction {

	/**
	 * Communication ID number (e.g. serial number, IP address, telephone number, etc.
	 * ) of the AMR module which serves this meter.
	 */
	public String amrAddress;
	/**
	 * Communication ID number (e.g. port number, serial number, data collector ID,
	 * etc.) of the parent device associated to this AMR module.
	 */
	public String amrRouter;
	/**
	 * Kind of communication direction.
	 */
	public ComDirectionKind direction;
	/**
	 * Kind of communication technology.
	 */
	public ComTechnologyKind technology;

	public ComFunction(){

	}
}//end ComFunction