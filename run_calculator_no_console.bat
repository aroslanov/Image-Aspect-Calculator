@echo off
REM Run AspectRatioCalculator GUI without a console window by using the venv's pythonw.exe
REM This script uses the repository root (the batch "parent" directory) as the working directory.

REM Get folder that contains this batch file (with trailing backslash)
setlocal enabledelayedexpansion
set "BASE_DIR=%~dp0"

REM Path to the virtual environment pythonw (more portable than activating venv)
set "VENV_PYTHONW=%BASE_DIR%\.venv\Scripts\pythonw.exe"

if exist "%VENV_PYTHONW%" goto :foundVenv
REM If venv pythonw doesn't exist, check PATH's pythonw
where pythonw >nul 2>&1
if !errorlevel! == 0 (
    set "PYTHONW=pythonw"
    goto :runCalc
)
echo ERROR: No pythonw found in repository venv or PATH. Please create the venv or install Python (with pythonw).
pause
exit /b 1

:foundVenv
set "PYTHONW=%VENV_PYTHONW%"

:runCalc

REM Launch the GUI using pythonw which doesn't open a console window.
REM The first quoted argument after start is the window title (empty), then the command and its arguments.
start "" "%PYTHONW%" "%BASE_DIR%calc.py"

endlocal
exit /b 0
