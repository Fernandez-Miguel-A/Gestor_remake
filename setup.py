from setuptools import setup
from Cython.Build import cythonize

##begin:

##setup(
##    name="pyDrillDown",
##    ext_modules=cythonize("pyDrillDown/**/*.py")
##)

##end

import glob
from setuptools import setup
from Cython.Build import cythonize

archivos = [
    f for f in glob.glob("pyDrillDown/**/*.py", recursive=True)
    if not f.endswith("__init__.py")
]

setup(
    name="pyDrillDown",
    ext_modules=cythonize(archivos, compiler_directives={'language_level': "3"}),
)

## comandos para crear las librerias y luego el ejecutable
## cmd-libs: py -3.13 setup.py build_ext build
## cmd-app1: auto-py-to-exe # cargar "librerias_pyd.json"
## cmd-app2: "librerias_pyd.bat"

