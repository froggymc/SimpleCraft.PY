python --version

if errorlevel == 1 goto installpython

pip help

if errorlevel == 1 goto installpip

pip install ursina

if errorlevel == 1 python3 simplecraft.py



python3 simplecraft.py