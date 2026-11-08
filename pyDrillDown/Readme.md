# Drilldown (Python / PySide6)

Versión en Python de la aplicación Qt original. La implementación modular está
en `.`, usa una base SQLite en memoria y contiene sus imágenes.

## Ejecutar

Requiere Python 3.10 o posterior.

```powershell
python -m pip install -r requirements.txt
python -m pyDrillDown.main
```

Haz clic en una imagen para cambiar su archivo o editar su descripción. Los
cambios se conservan mientras la aplicación está abierta.
