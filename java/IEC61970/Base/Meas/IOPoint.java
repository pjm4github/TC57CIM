package TC57CIM.IEC61970.Base.Meas;

import TC57CIM.IEC61970.Base.Core.IdentifiedObject;
import TC57CIM.IEC61970.Base.ICCPConfiguration.ProvidedBilateralPoint;

/**
 * The class describe a measurement or control value. The purpose is to enable
 * having attributes and associations common for measurement and control.
 * @author SELAOST1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class IOPoint extends IdentifiedObject {

	public ProvidedBilateralPoint BilateralToIOPoint;

	public IOPoint(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}