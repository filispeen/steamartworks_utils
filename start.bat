@echo off

set DIR=%~dp0
set PATH=%DIR%\venv;%DIR%\venv\Scripts;%PATH%
set PY_LIBS=%DIR%\venv\Scripts\Lib;%DIR%\venv\Scripts\Lib\site-packages
set PY_PIP=%DIR%\venv\Scripts
set SKIP_VENV=0
set PIP_INSTALLER_LOCATION=%DIR%\venv\get-pip.py

if not defined PYTHON (set PYTHON=python)
if not defined VENV_DIR (set "VENV_DIR=%~dp0%venv")

set PYTHON="%VENV_DIR%\Scripts\Python.exe"
call "%VENV_DIR%\Scripts\activate.bat"
echo venv %PYTHON%

call pip install uv==0.8.14
call uv pip install -r requirements.txt