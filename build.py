import os
import subprocess

cmd = subprocess.run(["git", "describe", "--abbrev=0"], stdout=subprocess.PIPE)
version: str = cmd.stdout.decode("utf-8")
version = version.strip()

with open("version.py", "w", encoding="utf8", errors="ignore") as f:
    f.write(f"version = {version}")

properties_file_content = ""
with open("build_properties_template.txt", 'r', encoding='utf8', errors='ignore') as f:
    properties_file_content = f.read()
properties_file_content = properties_file_content.replace("x.x.x.x", version)
with open("tmp_build_properties.txt", 'w', encoding='utf8') as f:
    f.write(properties_file_content)

os.system("pyinstaller --onefile main.py --version-file=\"tmp_build_properties.txt\"")
filename = "./dist/baldurs-gate-3-auto-join-conversations.exe"
if os.path.isfile(filename):
    os.remove(filename)
os.rename("./dist/main.exe", filename)

os.remove("tmp_build_properties.txt")