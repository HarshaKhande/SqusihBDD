@echo off
cd /d "%~dp0demo_site"
where py >nul 2>nul
if %errorlevel%==0 (
    py server.py
) else (
    python server.py
)
pause
