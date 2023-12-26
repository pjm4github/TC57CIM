package IEC62325.MarketOperations.MarketOpCommon;

import IEC61970.Base.Wires.Line;
import IEC62325.InfIEC62325.InfEnergyScheduling.TransmissionRightOfWay;

/**
 * Subclass for IEC61970:Wires:Line.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class MktLine extends Line {

	public TransmissionRightOfWay TransmissionRightOfWay;

	public MktLine(){

	}
}//end MktLine