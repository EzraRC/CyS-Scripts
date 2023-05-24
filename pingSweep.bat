:: This script pings a range of IP addresses and displays the result of each IP pinged

echo Starting ping sweep...
@echo off

:: Typical for loop
FOR /L %%i IN (1, 1, 254) DO (
    ping -a -n 1 192.168.1.%%i
)

:: Pauses the script so we can read the output after it's complete
pause

:: Please note that the script assumes the subnet mask to be 255.255.255.0, which is the common default subnet mask for a typical Class C IP address range like 192.168.1.x.
