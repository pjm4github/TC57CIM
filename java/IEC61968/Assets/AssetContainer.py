#######################################################
# 
# AssetContainer.py
# Python implementation of the Class AssetContainer
# Generated by Enterprise Architect
# Created on:      25-Dec-2023 8:45:19 PM
# 
#######################################################
from java.IEC61968.Assets import Seal
from java.IEC61968.Assets import Asset

class AssetContainer(Asset):
    """Asset that is aggregation of other assets such as conductors, transformers,
    switchgear, land, fences, buildings, equipment, vehicles, etc.
    """
    # All seals applied to this asset container.
    Seals= Seal()