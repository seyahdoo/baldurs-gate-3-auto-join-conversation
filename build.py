import os
import shutil
from version import version, minor, major, fix

build_properties = f"""
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({major},{minor},{fix},0),
    prodvers=({major},{minor},{fix},0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
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
        StringStruct(u'LegalCopyright', u'Seyahdoo Studios \\xa9'),
        StringStruct(u'OriginalFilename', u'baldurs-gate-3-auto-join-conversations.exe'),
        StringStruct(u'ProductName', u'Baldurs Gate 3 Auto Join Conversations'),
        StringStruct(u'ProductVersion', u'{version}')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
"""

text_file = open("build_properties.txt", "w")
n = text_file.write(build_properties)
text_file.close()

os.system("pip install -r requirements.txt")
os.system("pyinstaller --onefile main.py --version-file=\"build_properties.txt\" --name baldurs-gate-3-auto-join-conversations")
os.remove("build_properties.txt")

build_extras = [
  "settings.json"
]

for filename in os.listdir("."):
  if filename.startswith("listen-in"):
    build_extras.append(filename)

for file in build_extras:
  shutil.copyfile(file, f"dist/{file}")

import zipfile

with zipfile.ZipFile('dist/baldurs-gate-3-auto-join-conversations.zip', 'w') as myzip:
  myzip.write('dist/baldurs-gate-3-auto-join-conversations.exe', "baldurs-gate-3-auto-join-conversations.exe")
  for file in build_extras:
    myzip.write(f'dist/{file}', file)


