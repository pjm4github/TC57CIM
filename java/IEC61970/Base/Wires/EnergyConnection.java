package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Core.ConductingEquipment;
import TC57CIM.IEC61970.InfIEC61970.EnergyArea.EnergyComponent;

/**
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class EnergyConnection extends ConductingEquipment {

	public EnergyComponent m_EnergyComponent;

	public EnergyConnection(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}