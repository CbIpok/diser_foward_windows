@echo off
set PORT=65432

echo Looking for process using port %PORT%...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :%PORT%') do (
    set PID=%%a
    echo Process ID using port %PORT%: %PID%
)

if defined PID (
    echo Killing process with PID %PID%...
    taskkill /PID %PID% /F
    echo Port %PORT% is now free.
) else (
    echo No process is using port %PORT%.
)
