@echo off
cd /d "%~dp0"
echo Starting HexStrike AI Server...
.\hexstrike-env\Scripts\python.exe hexstrike_server.py --debug
pause
