package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MktDomain.AreaControlMode;
import IEC61970.Base.Domain.Frequency;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.PowerSystemResource;
import IEC62325.InfIEC62325.InfFinancial.ControlAreaOperator;
import IEC62325.MarketOperations.ParticipantInterfaces.BidSelfSched;
import IEC62325.MarketOperations.MarketSystem.MarketResults.LossClearingResults;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransferInterface;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.SysLoadDistributionFactor;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * A HostControlArea has a set of tie points and a set of generator controls (i.e.,
 * AGC). It also has a total load, including transmission and distribution losses.
 * @created 28-Dec-2023 12:15:02 PM
 */
public class HostControlArea extends PowerSystemResource {

	/**
	 * The area's present control mode: (CF = constant frequency) or (CTL = constant
	 * tie-line) or (TLB = tie-line bias) or (OFF = off control)
	 */
	public AreaControlMode areaControlMode;
	/**
	 * The present power system frequency set point for automatic generation control
	 */
	public Frequency freqSetPoint;
	/**
	 * The control area's frequency bias factor, in MW/0.1 Hz, for automatic
	 * generation control (AGC)
	 */
	public Float frequencyBiasFactor;
	public AdjacentCASet AdjacentCASet;
	/**
	 * A ControlAreaCompany controls a ControlArea.
	 */
	public ControlAreaOperator Controls;
	public Flowgate Flowgate;
	public CnodeDistributionFactor CnodeDistributionFactor;
	/**
	 * The interchange area  may operate as a control area
	 */
	public SubControlArea SubControlAreas;
	public BidSelfSched BidSelfSched;
	public LossClearingResults LossClearingResults;
	public TransferInterface TransferInterface;
	public SysLoadDistributionFactor SysLoadDistribuFactor;
	public RegisteredResource RegisteredResource;

	public HostControlArea(){

	}
}//end HostControlArea