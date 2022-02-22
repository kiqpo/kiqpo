#!/usr/bin/python3

# If any changes made to this file
# There is chance to brake for program.


# improting reqired modules
from curses import window
import sys
from multiprocessing import Process
import webbrowser
from desktop import app
from click import argument
from livereload import Server, shell
try:
    import main
except:
    pass
import inspect
import time
import asyncio
from importlib import reload


# color code


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# run app at first time, get initialCode
# only runing for first time,
try:
    main.RunApp()
except NameError as err:
    print()
    print(bcolors.FAIL, "Error:", err, bcolors.ENDC)
    print(bcolors.FAIL, "there fore server stop runing", bcolors.ENDC)
    sys.exit()


initialCode = inspect.getsource(main)

# loop one


def livekiqposerver():
    server = Server()
    server.watch('./kiqpo/native', shell('make html', cwd='native'))
    server.serve(root='./kiqpo/native', restart_delay=0)


def openwebbrowser():
    webbrowser.open("http://127.0.0.1:5500")


def codechanges():
    print()
    print(bcolors.HEADER, 'WELCOME TO KiQPO 0.1.0', bcolors.ENDC)
    print()
    print(bcolors.OKGREEN, "Compiled successfully!", bcolors.ENDC)
    print("____________________________________________________")
    print()

    async def getNewCode():
        # waiting to a new change in the user file ,code
        # if the change have been orcared run if else statement in the
        # getCode function and reload code(main.py) and run it.
        # useing async function , so that we have to wait to writing the new native file(.html)
        global NewCode
        global OsTimeInitial
        try:
            reload(main)
        except:
            pass
        time.sleep(00.1)
        NewCode = inspect.getsource(main)
        OsTimeInitial = time.time()

    def getCode():
        # if the new code have been founed
        #  take that and run main.RunApp()
        # funcation
        # then reload main.py
        global initialCode
        if NewCode != initialCode:
            # code have been changed
            # now let reflect code changes
            OsTimeNew = time.time()
            initialCode = inspect.getsource(main)
            # reflect code changes
            try:
                reload(main)
                main.RunApp()
            # prompt ui have been updated
                print()
                print(
                    f"{bcolors.OKGREEN}➤ changes updated in : {bcolors.ENDC}{OsTimeNew-OsTimeInitial}")
                print()
            except Exception as err:
                print(bcolors.FAIL, "➤ Error:", err, bcolors.ENDC)
            except:
                print(bcolors.FAIL, "➤ Error:",
                      "unknown error occurred", bcolors.ENDC)

    while True:
        try:
            asyncio.run(getNewCode())
        # wait to take lest changes
        # then call getCode fun
            getCode()
        except KeyboardInterrupt as err:
            print(bcolors.OKBLUE, "server stop runing ●", bcolors.ENDC)
            sys.exit()
        except:
            print(bcolors.FAIL, "Error:", "unknown error occurred", bcolors.ENDC)


# end if loader.py


def method():
    global runingmethod
    runingmethod = ""
    argumentlength = len(sys.argv)
    # print(sys.argv)
    methodName = sys.argv[argumentlength-1]
    if(methodName == 'run-web'):
        runingmethod = "WEB"
    elif(methodName == "run-desktop"):
        runingmethod = "DESKTOP"
    else:
        print(str(methodName+" is undefined,help wwww.github.com/kiqpo."))

    return runingmethod


# starting point
if __name__ == '__main__':
    runwith = method()
    if(runwith == "WEB"):
        # start livekiqposerver
        Process(target=livekiqposerver).start()
        # start compling
        Process(target=codechanges).start()
        # open browser
        Process(target=openwebbrowser).start()
    elif(runwith == "DESKTOP"):
        Process(target=codechanges).start()
        Process(target=app.main).start()
