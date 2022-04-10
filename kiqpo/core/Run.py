from .compiler import functions

def Run(python):
    try:
        return functions.py2js(python)
    except Exception as error:
        print(error)
