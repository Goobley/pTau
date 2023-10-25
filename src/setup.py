from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

extension = Extension("pTau",
                      sources=["pyTau.pyx"],
                      include_dirs=["./", numpy.get_include()],
                      language="c++",
                      extra_compile_args=["-fopenmp"],
                      extra_link_args=["-fopenmp"],
            )

p_tau_ext = cythonize([extension], language_level=3)

setup(
    name = 'pTau',
    version = '1.0',
    author = 'J. de la Cruz Rodriguez (ISP-SU 2021)',
    ext_modules=[extension],
)

