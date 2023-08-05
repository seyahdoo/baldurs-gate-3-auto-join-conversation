import os


os.system("pyinstaller --onefile main.py --version-file=\"build_properties.txt\"")
filename = "./dist/baldurs-gate-3-auto-join-conversations.exe"
if os.path.isfile(filename):
    os.remove(filename)
os.rename("./dist/main.exe", filename)
