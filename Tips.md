Setup

python -m venv {name} 
python -m venv venv

Activate the virtual env

source ./venv/bin/activate


Get PIP


Install Libraries (sometimes pip might be required to be updated)

pip uninstall playsound
pip install playsound

Or create a requirements.txt file for dependencies

Start program

python {name}.py


PIP Show Installed Libraries 
pip list

PIP Show details of a library
pip show gTTS

Create a dependency list requirements file
pip freeze > requirements.txt