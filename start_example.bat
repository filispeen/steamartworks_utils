@echo off

call %~dp0\env.bat

call python example.py
call python combine.py --base-dir %~dp0\example
call python resize_combined.py --base-dir %~dp0\example
call python crop.py --base-dir %~dp0\example
call python compress_parts.py --base-dir %~dp0\example
choice /c YN /M "Do you want to upload this example into your steam workshop"
if %ERRORLEVEL%==1 (
    call python steam_upload.py --base-dir %~dp0\example
) else ( exit /b 0 )