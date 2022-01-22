# This is Core code of hot reloading if any changes made to this file
# There is chance to brake for program


# improting reqired modules
from typing import Tuple
import sys
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


# prompt user that loader is runing
print(bcolors.HEADER, """


    **********************************************************************
    *                     Welcome to Kiqpo                               *
    *                       version 1.0                                  *
    *                                                                    *
    *                                                                    *
    *         crafting beautiful, fast user experiences for web          *
    **********************************************************************

 """, bcolors.ENDC)
print()
print(bcolors.OKGREEN, "server started successfully ✓", bcolors.ENDC)
print(bcolors.BOLD, "____________________________________________________", bcolors.BOLD)
print()
print("waiting for changes.")


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
            print(bcolors.FAIL, "➤ Error:", "unknown error occurred", bcolors.ENDC)


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
