#!/usr/bin/env python3

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os
import sys

def credentials():
    # github username and password
    credentials.username = ''
    credentials.password = ''
    # email and password
    credentials.email=''
    credentials.emailpassword=''
    # the directory of your folder from home
    credentials.websitefolder='websites'
    credentials.pythonfolder='python'
    credentials.flutterfolder='flutter'
    # chrome options 
    credentials.chromebin="/usr/bin/google-chrome"
    credentials.chromedriver='/usr/local/bin/chromedriver'
def setup():
    credentials()
    print('enter github credentials\n')
    credentials.username = input('please enter your username: ')
    credentials.password = input('please enter your password: ')
    
    if input('do you want to make additional changes?Y/n: ').lower()=='y':
        print('\n\n *** additional setup *** \n\n')
        print('website project folder: home/'+credentials.websitefolder)
        if input('is this ok?Y/n: ').lower()=='y':
            pass
        else:
            credentials.websitefolder=input('please enter the location of your website project folder: ')
        print('python project folder: home/'+credentials.pythonfolder)
        if input('is this ok?Y/n: ').lower()=='y':
            pass
        else:
            credentials.pythpnfolder=input('please enter the location of your website project folder: ')
        print('flutter project folder: home/'+credentials.flutterfolder)
        if input('is this ok?Y/n: ').lower()=='y':
            pass
        else:
            credentials.flutterfolder=input('please enter the location of your website project folder: ')

        print('location of your chrome bin/executable:'+credentials.chromebin)
        if input('is this ok?Y/n: ').lower()=='y':
            pass
        else:
            credentials.chromebin=input('please enter the location of your chrome bin/executable: ')
        print('location of chromedriver:'+credentials.flutterfolder)
        if input('is this ok?Y/n: ').lower()=='y':
            pass
        else:
            credentials.flutterfolder=input('please enter the location of your chromedriver: ')
    else:
        pass
    print('\n\n *** you are all done with the setup *** \n\n')
def chromeGmail(driver):
    driver.get('https://gmail.com')
    time.sleep(5)
    emailinput=driver.find_element_by_xpath('//*[@id="identifierId"]')
    emailinput.send_keys(credentials.email)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/span').click()

    passwordinput=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    passwordinput.send_keys(credentials.emailpassword)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/span').click()

    gitemail=driver.find_element_by_xpath('//*[@id=":2t"]')
    gitemail.click()
    time.sleep(4)
    verificationcodefull=driver.find_element_by_xpath('//*[@id=":no"]/text()')
    array=[]
    for word in verificationcodefull:
        array.append(word)
    code=[]
    code.append(array[-6]+array[-5]+array[-4]+array[-3]+array[-2]+array[-1])
    number=''
    for element in code:
        number+=element
    return number
def checkDir(projecttype):
    if projecttype=='website':
        projTypeFolder= credentials.websitefolder
    if projecttype=='python':
        projTypeFolder=credentials.pythonfolder
    if projecttype=='flutter':
        projTypeFolder=credentials.flutterfolder
    else:
        projTypeFolder=projecttype
    return projTypeFolder
def changedir(Ptype):
    myprojectname=create.reponame
    os.chdir(os.path.expanduser("~"))
    changedir.projecttype=Ptype
    # fetch new directory from user defined directories
    os.chdir(checkDir(changedir.projecttype)) 
    try:
        os.mkdir(myprojectname)
    except FileExistsError:
        print('folder already exists \n opening folder ...')
    os.chdir(myprojectname)
    # launch vs code in the project directory
    os.system('code .')
def checkproject(string):
    changedir(string)
    string.rstrip().lower()
    return string.rstrip().lower()
def listtostring(name):
    string=""
    for elements in name:
        string+=(elements+" ")
    return string

# create folder with the name and open
# def createDir():
    # command should be Create git [project type] [project name]
    # if website cd to the website directory, if python do the necessary, if flutter open flutter projects directory
def chromeGit(driver,gmaildriver):
    driver.get('https://github.com/')
    time.sleep(3) # Let the user actually see something!
    signin= driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
    signin.click()
    # now check to see if the progress bar has been compeleted
    time.sleep(5)
    usernameInput= driver.find_element_by_xpath('//*[@id="login_field"]')
    usernameInput.send_keys(credentials.username)
    time.sleep(3)
    passwordInput=driver.find_element_by_xpath('//*[@id="password"]')
    passwordInput.send_keys(credentials.password)
    time.sleep(3)
    signinBtn=driver.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[9]')
    signinBtn.click()
    time.sleep(5)
    # sometimes github needs verification. If that's the case tell the user and close the app
    try:
        newRepoBtn=driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a')
        newRepoBtn.click()
    except:
        print('Authentication required for browser.\n opening google chrome and getting required code')
        driver.find_element_by_xpath('//*[@id="otp"]').send_keys(chromeGmail(gmaildriver))
        driver.find_element_by_xpath('//*[@id="login"]/div[3]/form/button').click()

    time.sleep(4)
    # now enter the name of the repo here
    repoNameInput=driver.find_element_by_xpath('//*[@id="repository_name"]')
    repoNameInput.send_keys(create.reponame)
    time.sleep(5)
    createBtn=driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[3]/button')
    createBtn.click()
    time.sleep(5)
    # get current url
    chromeGit.projectUrl = driver.current_url
    # now close chrome
    driver.close()
    print("project url: "+chromeGit.projectUrl+"\nproject name: "+create.reponame+"\nproject type: "+checkproject(create.projecttype)+"\nOpening project on vs code ...")

def create():
 # get name from the script
    x=sys.argv
    y=sys.argv[1]
    x.pop(0)
    x.pop(0)
    create.reponame=listtostring(x).rstrip()
    create.projecttype=y.rstrip()
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    # options.add_argument("--headless")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument('--window-size=1420,1080')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.binary_location = credentials.chromebin
    # options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})

    # options.binary_location = "/snap/chromium/current/bin/chromium.desktop"
    driver = webdriver.Chrome(options=options, executable_path=credentials.chromedriver)
    gmaildriver = webdriver.Chrome(options=options, executable_path=credentials.chromedriver)
    # options.add_argument("--user-data-dir=/home/ubuntu/.config/google-chrome/Default") 
    # #Path to your chrome profile

    if not create.reponame:
        print('invalid repo name')
    else:
       chromeGit(driver,gmaildriver)
def arraytostring(arr):
    string=''
    for element in arr:
        string += element
    return string
def push():
    reverseuser=sys.argv[::-1]
    if arraytostring(sys.argv[-1]) == '-f' or '--force':
        gitlink=arraytostring(sys.argv[-2])
    else:
        gitlink=arraytostring(sys.argv[-1])
    x=sys.argv
    x.pop(-1)
    x.pop(0)
    commitname = listtostring(x)
    
    os.system('git init')

    # Adds the files in the local repository and stages them for commit. 
    # To unstage a file, use 'git reset HEAD YOUR-FILE'.

    os.system('git add .')
    os.system('git commit -m '+'"'+commitname+'"')
    # Commits the tracked changes and prepares them to be pushed to a remote repository.
    # To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.
    os.system('git remote add origin '+gitlink)
    # Sets the new remote

    # reverse the array first

    # now get the last element (first in the string)
    userstring=arraytostring(reverseuser[0])
    print('please confirm your identity')
    if arraytostring(userstring)=='-f' or arraytostring(userstring)=='--force':
        os.system('git push origin master -f')
    else:
        os.system('git push origin master')
    # Pushes the changes in your local repository up to the remote repository you specified as the origin 
def helpme():
    print('usage: easygit [--version] [--help]\nlisted below are the commands for easygit:\n')
    print('create [project type] [project name]       Create a project on github and open it on vscode working area')
    print('push [commit name] [project url] [force]       push a project to github. You can add --f or -force at the end. You can also leave the -f if it is not a forced update')
    print('--help or -h     show available options')

def tostring(usi):
    string=""
    for elements in usi:
        string+=elements
    return string
def main():
    userinput=sys.argv[1]
    ui=tostring(userinput)
    if ui=='help':
        helpme()
    
    if ui=='push':
        push()
    if ui=='create':
        print('\n enter the email address and password related to your github account\n')
        credentials.email=input('email address:')
        credentials.emailpassword=input('email password:')
        setup()
        create()
if __name__== "__main__" :
    main()
