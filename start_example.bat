@echo off

set DIR=%~dp0
call %DIR%env.bat

call python %DIR%scripts\example.py
call python %DIR%scripts\combine.py --base-dir %DIR%example
call python %DIR%scripts\resize_combined.py --base-dir %DIR%example
call python %DIR%scripts\crop.py --base-dir %DIR%example
call python %DIR%scripts\compress_parts.py --base-dir %DIR%example
choice /c YN /M "Do you want to upload this example into your steam workshop"
if %ERRORLEVEL%==1 (
    call python %DIR%scripts\steam_upload.py --base-dir %DIR%example
) else ( exit /b 0 )