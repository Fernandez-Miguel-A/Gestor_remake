from setuptools import setup
from Cython.Build import cythonize

setup(
    name="pyDrillDown",
    ext_modules=cythonize("pyDrillDown/**/*.py")
)

## comandos para crear las librerias y luego el ejecutable
## cmd-libs: py -3.13 setup.py build_ext build
## cmd-app1: auto-py-to-exe # cargar "librerias_pyd.json"
## cmd-app2: "librerias_pyd.bat"

