@echo off

FOR /L %%i IN (1, 1, 254) DO (
    ping -a -n 1 192.168.1.%%i
)

pause
