# QRCodeGenerateandRead Project

QRCodeGenerateandRead Project is coded with Python3, used Flask framework and Html mark-up language and deployed in Azure.
To access: http://2099190p.azurewebsites.net

## Installation

Follow instructions on:
(to run on local)
#In Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
FLASK_APP=application.py flask run

#In PowerShell
py -3 -m venv env
env\scripts\activate
pip install -r requirements.txt
Set-Item Env:FLASK_APP ".\application.py"
flask run

#Or you can follow instructions on:
https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-python


## Usage

Only allowed colors are Black, White, Red, Green and Turqoise, other text in 2 and 3 will give you an error

All fields denoted with * must be filled, otherwise you will get an error

Turqoise background colors may give an error sometimes


## License
Sinan Talha KOŞAR - GitHub.com/STalhaKOSAR