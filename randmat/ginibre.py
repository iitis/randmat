import numpy as np

@dataclass
class GinibreEnsemble:
    nrows: int
    ncols: int
    beta: int = 2

    @property
    def idim(self):
        return ncols

    @property
    def odim(self):
        return nrows