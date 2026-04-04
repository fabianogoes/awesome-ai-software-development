@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "PROFILE=%1"

if /I "%PROFILE%"=="--help" goto :help
if /I "%PROFILE%"=="-h" goto :help
if /I "%PROFILE%"=="help" goto :help

if "%PROFILE%"=="" set "PROFILE=minimal"

powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_DIR%setup-agents.ps1" -Profile "%PROFILE%"
exit /b %ERRORLEVEL%

:help
echo Usage:
echo   scripts\setup-agents.cmd [minimal^|standard^|full]
echo   scripts\setup-agents.cmd --help
echo.
echo Profiles:
echo   minimal   cria a base agnostica minima
echo   standard  adiciona docs operacionais, tools, images e extensoes de .agents
echo   full      adiciona templates opinativos para colaboracao e governanca
exit /b 0
