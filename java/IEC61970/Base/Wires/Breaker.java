

import TC57CIM.IEC61970.Base.Domain.Seconds;

/**
 * A mechanical switching device capable of making, carrying, and breaking
 * currents under normal circuit conditions and also making, carrying for a
 * specified time, and breaking currents under specified abnormal circuit
 * conditions e.g.  those of short circuit.
 * @author pmora
 * @updated 15-Dec-2023 1:39:41 PM
 */
public class Breaker extends ProtectedSwitch {

	/**
	 * The transition time from open to close.
	 */
	private Seconds inTransitTime;

	public Breaker(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public Seconds getinTransitTime(){
		return inTransitTime;
	}

	/**
	 * 
	 * @param newVal
	 */
	public void setinTransitTime(Seconds newVal){
		inTransitTime = newVal;
	}

}