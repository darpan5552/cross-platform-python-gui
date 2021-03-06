# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
from kivymd import hooks_path as kivymd_hooks_path

a = Analysis(['Desktop/main.py'],
             pathex=['/media/darpan/Motu/Softwares/Android/LinuxBuild'],
             binaries=[],
             datas=[('Desktop/matrixcalculator.kv','.'),('Desktop/assets','assets')],
             hiddenimports=[],
             hookspath=[kivymd_hooks_path],
             runtime_hooks=[],
             excludes=['numpy', 'docutils', 'pygments', 'PIL'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Matrix Calculator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=True,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False)
