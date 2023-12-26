package IEC62325.MarketOperations.MarketOpCommon;

import IEC62325.MarketOperations.ReferenceData.Flowgate;
import IEC61970.Base.Core.Terminal;

/**
 * Subclass of IEC61970:Core:Terminal.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class MktTerminal extends Terminal {

	public Flowgate Flowgate;

	public MktTerminal(){

	}
}//end MktTerminal