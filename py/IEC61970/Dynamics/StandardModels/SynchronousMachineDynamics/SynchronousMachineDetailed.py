from IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics.IfdBaseKind import IfdBaseKind
from IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics.SynchronousMachineDynamics import \
    SynchronousMachineDynamics


class SynchronousMachineDetailed(SynchronousMachineDynamics):
    """
    All synchronous machine detailed types use a subset of the same data parameters
    and input/output variables.
    The several variations differ in the following ways:
      <ul>
          <li>The number of equivalent windings that are included</li>
          <li>The way in which saturation is incorporated into the model.</li>
          <li>Whether-or-not "subtransient saliency" (X''q not = X''d) is represented.</li>
      </ul>
      <b>Note:</b> It is not necessary for each simulation tool to have separate
      models for each of the model types. The same model can often be used for
      several types by alternative logic within the model. Also, differences in
      saturation representation may not result in significant model performance
      differences so model substitutions are often acceptable.
      @author ppbr003
      @version 1.0
      @created 29-Dec-2023 11:24:20 PM
    """
    def __init__(self):
        # Ratio (Exciter voltage/Generator voltage) of Efd bases of exciter and generator models. Typical Value = 1.
        super().__init__()
        self.efd_base_ratio = 1.0

        # Excitation base system mode. It should be equal to the value of WLMDV given by the user.
        # WLMDV is the per-unit ratio between the field voltage and the excitation current: Efd = WLMDV*Ifd.
        # Typical Value = ifag.
        self.ifd_base_type = IfdBaseKind.IFAG

        # Q-axis saturation factor at 120% of rated terminal voltage (S12q) (>=S1q). Typical Value = 0.12.
        self.saturation_factor_120_q_axis = 0.12

        # Q-axis saturation factor at rated terminal voltage (S1q) (>= 0). Typical Value = 0.02.
        self.saturation_factor_q_axis = 0.02

