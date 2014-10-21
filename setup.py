from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

# sourcefiles_e = ['example.pyx','stdsage.c','interrupt.c','mpz_pylong.c','mpn_pylong.c']
# sourcefiles_p = ['pari_instance.pyx','stdsage.c','interrupt.c','mpz_pylong.c','mpn_pylong.c']
# sourcefiles_p = ['handle_error.pyx','stdsage.c','interrupt.c','mpz_pylong.c','mpn_pylong.c']

# setup(#name="example",
#     #cmdclass = {'build_ext': build_ext},
#     ext_modules = cythonize([Extension("example", sourcefiles_e,libraries=["pari","gmp","m"]),Extension("pari_instance", sourcefiles_p,libraries=["pari","gmp","m"]) ])
# )

#example.pyx','pari_instance.pyx','handle_error.pyx
sourcefiles = ['stdsage.c','interrupt.c','mpz_pylong.c','mpn_pylong.c']

setup(name="par",
    cmdclass = {'build_ext': build_ext},
    ext_modules = cythonize([
        Extension('gen', 
                  sources = ["gen.pyx"],
                  libraries = ['pari', 'gmp',"m","csage"],extra_link_args=["-Lbuild/lib.linux-x86_64-2.7"]),
        #,extra_compile_args=[ "-Og"],extra_link_args=["-Og"]),
        Extension('handle_error',
                  sources = ["handle_error.pyx"],
                  libraries = ['pari', 'gmp',"m","csage"],extra_link_args=["-Lbuild/lib.linux-x86_64-2.7"]),#,extra_compile_args=[ "-Og"],extra_link_args=["-Og"]),
        Extension('pari_instance',
                  sources = ["pari_instance.pyx"],
                  libraries = ['pari', 'gmp',"m","csage"],extra_link_args=["-Lbuild/lib.linux-x86_64-2.7"]),
        Extension('csage',
                  sources=['stdsage.c','interrupt.c','mpz_pylong.c','mpn_pylong.c','memory.c'],
                  libraries=['gmp'])])#,extra_compile_args=[ "-Og"],extra_link_args=["-Og"])])
)
