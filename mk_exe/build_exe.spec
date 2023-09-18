########spec file##########

# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [('D:\\Python\\tools\\extract_draw\\Tesseract-OCR500\\tessdata\\','data\\tessdata'),('D:\Grabby\search.ico','.')]
binaries = [('D:\\Python\\tools\\extract_draw\\Tesseract-OCR500\\', 'tesseract')]
hiddenimports = []
tmp_ret = collect_all('pyocr')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

block_cipher = None

a = Analysis(['getControl.py'],
            pathex=['D:\\Grabby'],
            binaries=binaries,
            datas=datas,
            hiddenimports=hiddenimports,
            hookspath=[],
            hooksconfig={},
            runtime_hooks=[],
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
         name='getControl',
         debug=False,
         bootloader_ignore_signals=False,
         strip=False,
         upx=True,
         console=True,
         disable_windowed_traceback=False,
         target_arch=None,
         codesign_identity=None,
         entitlements_file=None , icon='search.ico')
coll = COLLECT(exe,
              a.binaries,
              a.zipfiles,
              a.datas, 
              strip=False,
              upx=True,
              upx_exclude=[],
              name='getControl')
