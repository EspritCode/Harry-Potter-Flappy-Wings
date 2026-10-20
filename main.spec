# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('fond_chateau.png', '.'), ('fond_chateau_clair.png', '.'), ('harry_transparent.png', '.'), ('HarryPotter.png', '.'), ('sorciere_rouge_droite.png', '.'), ('sorciere_rouge_gauche (1).png', '.'), ('sorciere_verte_droite.png', '.'), ('sorciere_verte_gauche.png', '.'), ('sorciere_violette_droite.png', '.'), ('sorciere_violette_gauche.png', '.')],
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
    a.binaries,
    a.datas,
    [],
    name='HarryPotter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
