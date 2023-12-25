from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.CatalogAssetType import CatalogAssetType
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance


class GeneratorTypeAsset(CatalogAssetType):
    """
    Generic generation equipment that may be used for various purposes such as work
    planning. It defines both the Real and Reactive power properties (modelled at
    the PSR level as a GeneratingUnit + SynchronousMachine).
    """

    def __init__(self):
        """
        Constructor for GeneratorTypeAsset.
        """
        super().__init__()
        self.max_p = ActivePower()
        """
        Maximum real power limit.
        """

        self.max_q = ReactivePower()
        """
        Maximum reactive power limit.
        """

        self.min_p = ActivePower()
        """
        Minimum real power generated.
        """

        self.min_q = ReactivePower()
        """
        Minimum reactive power generated.
        """

        self.r_direct_subtrans = Resistance()
        """
        Direct-axis subtransient resistance.
        """

        self.r_direct_sync = Resistance()
        """
        Direct-axis synchronous resistance.
        """

        self.r_direct_trans = Resistance()
        """
        Direct-axis transient resistance.
        """

        self.r_quad_subtrans = Resistance()
        """
        Quadrature-axis subtransient resistance.
        """

        self.r_quad_sync = Resistance()
        """
        Quadrature-axis synchronous resistance.
        """

        self.r_quad_trans = Resistance()
        """
        Quadrature-axis transient resistance.
        """

        self.x_direct_subtrans = Reactance()
        """
        Direct-axis subtransient reactance.
        """

        self.x_direct_sync = Reactance()
        """
        Direct-axis synchronous reactance.
        """

        self.x_direct_trans = Reactance()
        """
        Direct-axis transient reactance.
        """

        self.x_quad_subtrans = Reactance()
        """
        Quadrature-axis subtransient reactance.
        """

        self.x_quad_sync = Reactance()
        """
        Quadrature-axis synchronous reactance.
        """

        self.x_quad_trans = Reactance()
        """
        Quadrature-axis transient reactance.
        """
