# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['E:\\xampp\\htdocs\\shop\\src\\main\\python\\main.py'],
             pathex=['E:\\xampp\\htdocs\\shop\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\users\\dell\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['E:\\xampp\\htdocs\\shop\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Shopee',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='E:\\xampp\\htdocs\\shop\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='Shopee')
