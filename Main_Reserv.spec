# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/MIGUEL A. FERNANDEZ/Desktop/Trabajos_Varios/Gestor_nuevo/Gestor_remake/Main_Reserv.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/MIGUEL A. FERNANDEZ/Desktop/Trabajos_Varios/Gestor_nuevo/Gestor_remake/pyDrillDown', 'pyDrillDown')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Main_Reserv',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:/ghidra_12.2_PUBLIC_20261016/ghidra_12.2_PUBLIC/support/ghidra.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Main_Reserv',
)
