from distutils.core import setup
from Cython.Build import cythonize
from Cython.Compiler.Nodes import cython_view_utility_code

setup(
    ext_modules= cythonize("sieve_module.py")
)