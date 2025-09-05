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

if "%*"=="" (
  echo If you need to process specific folder with your images. Drag and drop folder into this batch file.
  timeout /t 3 /nobreak > nul
  call %PYTHON% combine.py
    call %PYTHON% resize_combined.py
    call %PYTHON% crop.py
    call %PYTHON% compress_parts.py
) else (
    for %%F in (%*) do (
        echo Processing folder: %%F
        call %PYTHON% combine.py --base-dir %%F
        call %PYTHON% resize_combined.py --base-dir %%F
        call %PYTHON% crop.py --base-dir %%F
        call %PYTHON% compress_parts.py --base-dir %%F
    )
)