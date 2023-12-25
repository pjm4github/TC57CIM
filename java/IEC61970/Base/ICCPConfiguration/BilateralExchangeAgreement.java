package TC57CIM.IEC61970.Base.ICCPConfiguration;

import TC57CIM.IEC61970.Base.Core.IdentifiedObject;

/**
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class BilateralExchangeAgreement extends IdentifiedObject {

	public BilateralExchangeActor Consumer;
	public BilateralExchangeActor Provider;

	public BilateralExchangeAgreement(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}