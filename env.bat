@echo off
setlocal

set DIR=%~dp0
set VENV_DIR=%DIR%\venv

call "%VENV_DIR%\Scripts\activate.bat"

if not defined PYTHON (set PYTHON=python)
if not defined VENV_DIR (set "VENV_DIR=%~dp0%venv")

setx PYTHON "%VENV_DIR%\Scripts\Python.exe"
setx PIP "%VENV_DIR%\Scripts\pip.exe"

call %pip% install uv
call uv pip install -r requirements.txt