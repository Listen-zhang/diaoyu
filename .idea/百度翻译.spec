# -*- mode: python -*-

block_cipher = None


a = Analysis(['�ٶȷ���.py'],
             pathex=['C:\\Users\\29722\\Desktop\\Python\\untitled1\\.idea'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='�ٶȷ���',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
