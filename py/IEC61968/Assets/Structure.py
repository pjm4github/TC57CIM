from IEC61968.Assets.AssetContainer import AssetContainer
from IEC61970.Base.Domain.Length import Length
from IEC61970.Base.Domain.Voltage import Voltage


class Structure(AssetContainer):
	"""
	# /**
	#  * Construction holding assets such as conductors, transformers, switchgear, etc.
	#  * Where applicable, number of conductors can be derived from the number of
	#  * associated wire spacing instances.
	#  */
	"""
	def __init__(self):
		super().__init__()
		self.fumigant_applied_date = Date()  # Date fumigant was last applied.
		self.fumigant_name = ""  # Name of fumigant.
		self.height = Length()
		# 	 * Visible height of structure above ground level for overhead construction (e.g.,
		# 	 * Pole or Tower) or below ground level for an underground vault, manhole, etc.
		# 	 * Refer to associated DimensionPropertiesInfo for other types of dimensions.
		# 	 */

		self.material_kind = StructureMaterialKind()  # Material this structure is made of.
		self.rated_voltage = Voltage()   # Maximum rated voltage of the equipment that can be mounted on/contained within
		# 	 * the structure.
		# 	 */
		self.remove_weed = True   # True if weeds are to be removed around asset.
		self.weed_removed_date = Date()  # Date weed were last removed.
		self.structure_supports = StructureSupport()

	def __del__(self):
		pass
