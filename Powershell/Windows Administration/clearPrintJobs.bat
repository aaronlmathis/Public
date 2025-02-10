@echo off
:: Check for Administrator privileges
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo This script requires Administrator privileges.
    echo Right-click and select "Run as administrator."
    pause
    exit /b
)

:: Run the PowerShell script with ExecutionPolicy Bypass
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0ClearPrintSpooler.ps1"
