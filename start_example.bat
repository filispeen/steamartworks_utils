@echo off

call env.bat

where ffmpeg.exe >nul 2>&1
if %ERRORLEVEL%==1 (
    call winget install Gyan.FFmpeg -h --accept-source-agreements --accept-package-agreements
    start cmd /k "pushd %~dp0 & start_example.bat"
    exit /b
)

call python example.py
call python combine.py
call python resize_combined.py
call python crop.py
call python compress_parts.py
choice /c YN /M "Do you want to upload this example into your steam workshop"
if %ERRORLEVEL%==1 (
    where chromedriver.exe >nul 2>&1
    if %ERRORLEVEL%==1 (
        call winget install Chromium.ChromeDriver -h --accept-source-agreements --accept-package-agreements
        start cmd /k "pushd %~dp0 & python steam_upload.py"
        exit /b
    )
    call python steam_upload.py
)