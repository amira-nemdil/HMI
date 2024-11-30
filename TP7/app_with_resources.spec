# app_with_resources.spec
block_cipher = None

a = Analysis(
    ['app_with_resources.py'],  # Your Python script
    pathex=[],  # Add paths if needed
    binaries=[],
    datas=[
        (r'C:\\nitro\\HMI\\TP7\\icons\\computer-cloud.png', 'icons'),
        (r'C:\\nitro\\HMI\\TP7\\icons\\burn.png', 'icons')
    ],  # Explicitly reference your PNG files
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ResourceApp',  # Name of your app
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to True for debugging
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=r'C:\\nitro\\HMI\\TP7\\icons\\computer-cloud.png'  # Adjust path and format
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ResourceApp'
)
