from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy
import os
import sys

USE_OPENMP = True
if "DISABLE_OPENMP" in os.environ:
    USE_OPENMP = False

# NOTE(cmo): Disable OpenMP by default on macOS... the compilers are too much
# pain for most people.
if sys.platform == 'darwin' and "ENABLE_OPENMP" not in os.environ:
    USE_OPENMP = False

compile_args = []
link_args = []
if USE_OPENMP:
    compile_args += ["-fopenmp"]
    link_args += ["-fopenmp"],


extension = Extension("pTau",
                      sources=["pyTau.pyx"],
                      include_dirs=["./", numpy.get_include()],
                      language="c++",
                      extra_compile_args=compile_args,
                      extra_link_args=link_args,
            )

p_tau_ext = cythonize([extension], language_level=3)

setup(
    name = 'pTau',
    version = '1.0',
    author = 'J. de la Cruz Rodriguez (ISP-SU 2021)',
    ext_modules=p_tau_ext,
)

