Contributors: Daniel Espiritu, Ara Chobanyan, Matthew Yom, Jian Wang, Peng Tang

In this project, we created a forecasting random forest algorithm along with a long short-term memory (LSTM) model that is able to predict the probability of an earthquake happening given a location, time, and magnitude. 

All dependencies are listed in the requirements.txt file, along with the versions used as of July 6, 2025. The detailed steps to get this project running on your machine is detailed below: 


OS-SPECIFIC INSTRUCTIONS

MacOS: 
    1. create a virtual environment named .venv by first opening a terminal to the project folder, and then type the command 'python3 -m venv .venv'. With this, your virtual environment is created. After that, activate the newly created venv using the command '.venv/bin/activate'. 

    2. ensure that the python interpreter that you are using is version 3.10
    
    2. now that the venv is made, download all of the dependencies included in the requirements.txt file by typing into the terminal 'pip install -r requirements.txt'

    3. if there are problems installing those packages it may be because you already have those dependencies downloaded, and a quick fix would be to type into the terminal 'pip install --force-reinstall -v -r requirements.txt' which uninstalls and reinstalls all packages

    4. enjoy!

Windows: 
