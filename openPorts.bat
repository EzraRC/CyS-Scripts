:: This script scans the ports of one IP address, and prints if the current port is Open

@echo off

:: IP Address variable, change if necessary.
set "ip=192.168.1.1"

:: For loop from 1 to 100 inclusive
powershell.exe -Command "for ($port=1; $port -le 100; $port++) {

	:: Tests the connection to the IP address and port.
	if (Test-NetConnection -ComputerName '%ip%' -Port $port -InformationLevel Quiet) {

		:: Print that the port is open.
		echo Port $port is open.
	}
}

::Pauses the script so we can read the output after it's complete.
pause
