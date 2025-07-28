@echo off
title IRON DAEMON
echo.
echo [IRON DAEMON] Verificando Python...
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no está instalado. Descárgalo desde https://www.python.org
    pause
    exit /b
)
echo [OK] Python detectado.
echo.
echo [IRON DAEMON] Instalando dependencias...
python -m pip install pysmb >nul 2>&1
echo [IRON DAEMON] Ejecutando herramienta...
python IronDaemon_Menu.py
pause
