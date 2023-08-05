import os


os.system("pyinstaller --onefile --add-data=\"listen-in.png;.\" main.py --version-file=\"build_properties_template.txt\"")
filename = "./dist/baldurs-gate-3-auto-join-conversations.exe"
if os.path.isfile(filename):
    os.remove(filename)
os.rename("./dist/main.exe", filename)
