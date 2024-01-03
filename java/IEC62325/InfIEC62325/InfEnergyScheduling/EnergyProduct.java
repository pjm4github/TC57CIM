package IEC62325.InfIEC62325.InfEnergyScheduling;

import IEC62325.InfIEC62325.InfFinancial.Marketer;
import IEC62325.InfIEC62325.InfFinancial.GenerationProvider;
import IEC61968.Common.Agreement;

/**
 * An EnergyProduct is offered commercially as a ContractOrTariff.
 * @created 03-Jan-2024 1:49:41 PM
 */
public class EnergyProduct extends Agreement {

	/**
	 * A Marketer may resell an EnergyProduct.
	 */
	public Marketer ResoldBy_Marketer;
	public GenerationProvider GenerationProvider;
	/**
	 * A Marketer holds title to an EnergyProduct.
	 */
	public Marketer TitleHeldBy_Marketer;

	public EnergyProduct(){

	}
}//end EnergyProduct