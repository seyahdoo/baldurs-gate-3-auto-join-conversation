# Baldurs Gate 3 Auto Join Conversation Script
auto joins conversation on baldurs gate 3 game

## How To Use

- Download baldurs-gate-3-auto-join-conversations.zip from latest release
- Extract to a folder
- Adjust settings.json
- Run baldurs-gate-3-auto-join-conversations.exe
- Use `Ctrl+Shift+P` to pause/unpause the script (Can be changed in settings.json)

## Known Problems

- The script might not be able to see your game on some cases. I'm not sure exactly when but try setting the game to borderless windowed or windowed mode, that helped in some cases.
- This script will take a screenshot of the game every one second and will analyze it. It may impact game performance.
- Using venv on build.py does not work. For build.py to work you gotta install the requirements on python global packages then run build.py with your main python executable. (don't use venv on builds)

## How To Setup Development Environment

- Install python 3.x
- Run pip install -r requirements.txt
- Run main.py normally or with python debugger

## How To Build locally

- Install python 3.x
- Run build.py (using venv on build.py does not work)
- Locate the build output at "dist/baldurs-gate-3-auto-join-conversations.zip"

## Create new Release

- Change version.py
- Push to main
- GitHub Actions will create and upload a new release
