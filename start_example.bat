@echo off
setlocal

call %~dp0\env.bat

call python example.py
call python combine.py
call python resize_combined.py
call python crop.py
call python compress_parts.py
choice /c YN /M "Do you want to upload this example into your steam workshop"
if %ERRORLEVEL%==1 (
    call python steam_upload.py
) else ( exit /b 0 )