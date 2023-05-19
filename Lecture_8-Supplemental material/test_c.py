import ctypes 

_libc = ctypes.CDLL('./test_c.so')
c_double_p = ctypes.POINTER(ctypes.c_double)
_libc.somma.argtypes = [ ctypes.c_int, ctypes.c_int, c_double_p, c_double_p]
_libc.somma.restype = ctypes.c_double


def somma(a, b):
    a.dtype = ctypes.c_double
    b.dtype = ctypes.c_double
    M, N = a.shape
    s = _libc.somma( ctypes.c_int(M), ctypes.c_int(N), 
                 a.ctypes.data_as(c_double_p), 
                 b.ctypes.data_as(c_double_p))
                 
    return s
