# easy git

![chromedriver:80.0.3987.106](https://img.shields.io/badge/chromedriver-80.0.3987.106-blue)
![python:3.7.3](https://img.shields.io/badge/python-3.7.3-blue)
![build:passing](https://img.shields.io/badge/build-passing-green)
![coverage:76%](https://img.shields.io/badge/coverage-76%25-yellowgreen)
![selenium:3.141.0](https://img.shields.io/badge/selenium-3.141.0-black)


**easygit is an automation software for github.**

I created the project to help me easily create a gihub project, create a local directory based on the project type/language and open vs code with all with one command.

``easygit create python easygit``

Also easy git can push the initialize, add origin, commit and push a project to github, all with one command

``easygit push initial-commit https://github.com/leonkoech/easygit``

you can force a push by adding '-f' or '--force'

``easygit push initial-commit https://github.com/leonkoech/easygit -f``

# requirements

easygit requires the following to run

*selenium 3.141.0 [documentation](https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.current_url)[download](https://pypi.org/project/selenium/)

*chrome version 80 [download](https://www.google.com/chrome/?brand=CHBD&gclid=CjwKCAjwpqv0BRABEiwA-TySwcmdG9S6AfkK0EmkAgCUchDrG_NLrQmbyZ5PcTMYACxK2po4Tsq5nhoCZh0QAvD_BwE&gclsrc=aw.ds)

*chromedriver 80.0.3987.106[download](https://chromedriver.chromium.org/downloads)
python 3.7.3+ [download](https://www.python.org/downloads/)

# setup

I created easygit on ubuntu. 
To enable easygit to run on other operating systems there are additional settings you have to modify.

1. when running the project to push or create, you'll get this after verifying your credentials. Type Y.

    ``do you want to make additional changes?Y/n: ``

2. select the documents where you should store your folders. The main directory is home. If you wish to change the directory    select yes. Do this for all the three folders.

    ``python project folder: home/python``

3. type n when asked the following and type the location of your google chrome executable

    ``
    location of your chrome bin/executable: /usr/bin/google-chrome
    is this ok?Y/n
    ``
4. type n when asked the following and type the location of your chrome driver

    ``
    location of your chromedriver: /usr/local/bin/chromedriver
    is this ok?Y/n
    ``

# installation

This is the fun part. Making easygit acessible through the terminal.
Also a disclaimer of sorts, this installation is for linux systems. Please look on how to make a python script executable for your operating system.

1. clone easygit project to a directory of your choice and open the easygit folder. 

    ``easygit/easygit``

2. run the following command in a terminal

    ``chmod +x easygit.py``

3. edit the shebang - *the **!/usr/bin/env python3** at the top to match the location of your python environment. Though this shebang should work on both mac and linux systems*

4. drop the .py extension by running the following command

    ``mv easygit.py easygit``

5. Now add easy git to your path. Start by creating bin directory if you don't already have it. It's in home/bin
        create bin
    ``mkdir -p ~/bin``
        or  continue if bin already exists

6. copy script to bin

    ``cp easygit ~/bin``

7. finally add it to your path. You can either add it temporarily or permanently.
        to add it temporarily run the folowing command
    ``export PATH=$PATH"=$HOME/bin"``
        to add it permanently 
    ``echo 'export PATH=$PATH":$HOME/bin"' >> .profile``
        refresh terminal with the following commannd OR just open a new terminal
    ``source .profile``
# screenshots



# contribution

If you would like to contribute to the project you can reach me via [email](mailto:leonkipkip@gmail.com)
Read the [contribution guide](https://github.com/leonkoech/easygit/contributions.md)

# license

This project is under the [MIT license](https://github.com/leonkoech/easygit/license.md)

