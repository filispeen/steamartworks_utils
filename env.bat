@echo off
setlocal

set DIR=%~dp0
set PATH=%PATH%;%DIR%\.venv\Scripts\

if exist %DIR%\.venv\ (
    echo "Activating virtual environment..."
    call %DIR%\.venv\Scripts\activate.bat
    set PYTHON=%DIR%\.venv\Scripts\python.exe
    echo "Virtual environment activated."
) else (
    echo "Creating virtual environment..."
    call python -m venv .venv
    set PYTHON=%DIR%\.venv\Scripts\python.exe
    call %DIR%\.venv\Scripts\activate.bat
    echo "Virtual environment created and activated."
)

call %PYTHON% -m pip install --upgrade pip
call %PYTHON% -m pip install uv
call %PYTHON% -m uv pip install -r requirements.txt
call %PYTHON% ./modules/ffmpeg_.py --path %DIR%.venv\Scripts\