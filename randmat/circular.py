import numpy as np
from .ginibre import GinibreEnsemble

class CircularEnsemble:
    def __init__(self, d):
        self.d = d
        self.g = GinibreEnsemble(d, d, 2)