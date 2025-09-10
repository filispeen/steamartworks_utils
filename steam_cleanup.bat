@echo off

set DIR=%~dp0
set venv_activate_script=%DIR%.venv\Scripts\activate.bat

if exist "%DIR%.venv\" (
    call "%venv_activate_script%"
    set PYTHON=%DIR%.venv\Scripts\python.exe
) else (
    call python -m venv .venv
    set PYTHON=%DIR%.venv\Scripts\python.exe
    call "%venv_activate_script%"
)

call %PYTHON% ./modules/ffmpeg_.py --path %DIR%.venv\Scripts\

call %PYTHON% %DIR%scripts\steam_cleanup.py