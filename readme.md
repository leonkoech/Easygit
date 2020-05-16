# Easy git

![chromedriver:80.0.3987.106](https://img.shields.io/badge/chromedriver-80.0.3987.106-blue)
![python:3.7.3](https://img.shields.io/badge/python-3.7.3-blue)
![build:passing](https://img.shields.io/badge/build-passing-green)
![selenium:3.141.0](https://img.shields.io/badge/selenium-3.141.0-black)
![coverage:76%](https://img.shields.io/badge/coverage-76%25-yellowgreen)


**easygit is an automation software for github.**

I created the project to help me easily create a github project and push the project to github.

The ```create``` command creates the project on a browser then creates a local directory based on the project type/language and opens vs code.

The ```push``` command simply pushes a project to github.


### Listed below are the commands you can use for easygit:

- Get current version of easygit:

    ```easygit [-version] or easygit [-V]```


- Show available options:

    ```easygit [-help] or  easygit [-h]```


- Create a project on github and open it on vscode working area:

    ```easygit create [project type] [project name]```


- Push a exisiting project to github:

   ```push ["commit name"] [project url]```

    You can add -f or -force at the end. 

    ```easygit push ["commit name"] [project url] -f```

    ***Note: The commit name should be in either single or double quotation marks.
          Forcing an Update is Optional***


- Reverse/remove git init:

    ```easygit [reverse]```

    use this command if you accidentally ran 'git init' or you accidentlly ran 'easygit push'


- Unstage a file:

    ```essygit [reset] ["name of file"]```

    ***note: name of file should also include the location. 
    For example "main/test.py" if the terminal directory is not the "main" directory but it's parent***

## Requirements

Easygit requires the following to run

* selenium 3.141.0 --> [Documentation](https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.current_url) --> [Download](https://pypi.org/project/selenium/)

* chrome version 80 --> [Download](https://www.google.com/chrome/?brand=CHBD&gclid=CjwKCAjwpqv0BRABEiwA-TySwcmdG9S6AfkK0EmkAgCUchDrG_NLrQmbyZ5PcTMYACxK2po4Tsq5nhoCZh0QAvD_BwE&gclsrc=aw.ds)

* chromedriver 80.0.3987.106 --> [Download](https://chromedriver.chromium.org/downloads)
python 3.7.3+ [download](https://www.python.org/downloads/)

## Installation

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
    
## Setup

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
Note: The program runs and you can see

## Screenshots

screenshot of ``easygit push`` at work.

![Screenshot from 2020-04-06 19-27-24](https://user-images.githubusercontent.com/39020723/78583577-af725580-783f-11ea-9f19-43f9a0825704.png | width=100)

video of ``easygit create`` at work

[video link](https://drive.google.com/open?id=1Su6NFtj0D7G-_F6UInyp0BNprxNekyt3)


## Contribution

If you would like to contribute to the project you can reach me via [email](mailto:leonkipkip@gmail.com)
Read the [contribution guide](https://github.com/leonkoech/easygit/contributions.md)

## License

This project is under the [MIT license](https://github.com/leonkoech/easygit/license.md)

## Issues

At this point in time making too much login requests to git activates two factor authentication. Where it sends an email with the code. I made a workaround for this by opening the gmail account it sent the link to and getting the link then pasting it to the github page.
I could not test this a lot of times to debug it because gmail also realised it was an autonomous program. For some reason gmail does not like autonomous  programs (that are not theirs).

edit: After some time of not using this script to log in 100 times a day!! , because I loved seeing it working, github realized I am a human being and it now works as it should. The above issue was nothing to be scared of to begin with.

I will be personally maintaining this project so feel free to Label issues and pull requests.

## Updates

Users can now undo ```git init``` and ```git add .```
Also, I fixed some minor bugs in the ```easygit push``` command.

