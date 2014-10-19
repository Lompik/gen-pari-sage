from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

sourcefiles = ['example.pyx','stdsage.c','interrupt.c']

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("example", sourcefiles,libraries=["pari","gmp","m"])]
)
