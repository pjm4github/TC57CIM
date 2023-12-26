package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.RealEnergy;
import IEC61970.Base.Domain.Currency;
import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Domain.Float;

/**
 * Unit for accounting; use either 'energyUnit' or 'currencyUnit' to specify the
 * unit for 'value'.
 * @created 25-Dec-2023 8:45:18 PM
 */
public class AccountingUnit {

	/**
	 * Unit of service.
	 */
	public RealEnergy energyUnit;
	/**
	 * Unit of currency.
	 */
	public Currency monetaryUnit;
	/**
	 * Multiplier for the 'energyUnit' or 'monetaryUnit'.
	 */
	public UnitMultiplier multiplier;
	/**
	 * Value expressed in applicable units.
	 */
	public Float value;

	public AccountingUnit(){

	}
}//end AccountingUnit