import numpy as np

def qr_fix(z):
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    ph = d/abs(d)
    idim = r.shape[0]
    q = q[:, 1:idim]
    q = ph * q
    return q