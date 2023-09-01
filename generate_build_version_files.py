from version import major, minor, fix, version

# Generate build.spec
with open("build.spec", "w") as f:
    f.write(f"""
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['main.py'],
             pathex=['.'],
             binaries=[],
             datas=[('listen-in-*.png', '.'), ('settings.json', '.'), ('requirements.txt', '.')])

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='baldurs-gate-3-auto-join-conversation',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          version='version_info.txt')
    """)

# Generate version_info.txt
with open("version_info.txt", "w") as f:
    f.write(f"""VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({major}, {minor}, {fix}, 0),
    prodvers=({major}, {minor}, {fix}, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Seyahdoo Studios'),
        StringStruct(u'FileDescription', u'Baldurs Gate 3 Auto Join Conversations Executable'),
        StringStruct(u'FileVersion', u'{version}'),
        StringStruct(u'InternalName', u'cmd'),
        StringStruct(u'LegalCopyright', u'Seyahdoo Studios \\\\xa9'),
        StringStruct(u'OriginalFilename', u'baldurs-gate-3-auto-join-conversation.exe'),
        StringStruct(u'ProductName', u'Baldurs Gate 3 Auto Join Conversations'),
        StringStruct(u'ProductVersion', u'{version}')])
      ] 
    ), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)""")

print("Generated build.spec and version_info.txt")
