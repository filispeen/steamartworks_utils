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
  call %PYTHON% %DIR%scripts\combine.py
  call %PYTHON% %DIR%scripts\resize_combined.py
  call %PYTHON% %DIR%scripts\crop.py
  call %PYTHON% %DIR%scripts\compress_parts.py
) else (
    for %%F in (%*) do (
        echo Processing folder: %%F
        call %PYTHON% %DIR%scripts\combine.py --base-dir %%F
        call %PYTHON% %DIR%scripts\resize_combined.py --base-dir %%F
        call %PYTHON% %DIR%scripts\crop.py --base-dir %%F
        call %PYTHON% %DIR%scripts\compress_parts.py --base-dir %%F
    )
)