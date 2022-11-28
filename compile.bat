@echo off
py -m nuitka main.py --standalone --onefile --windows-icon-from-ico=icon.ico --enable-plugin=tk-inter --windows-disable-console -o "Random Coordinates.exe"
pause