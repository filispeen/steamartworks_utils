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
  call %PYTHON% steam_upload.py
) else (
    for %%F in (%*) do (
        echo Uploading folder: %%F
        call %PYTHON% steam_upload.py --base-dir %%F
    )
)