from dataclasses import dataclass

# import numpy as np


@dataclass
class GinibreEnsemble:
    nrows: int
    ncols: int
    beta: int = 2

    @property
    def idim(self):
        return self.ncols

    @property
    def odim(self):
        return self.nrows
