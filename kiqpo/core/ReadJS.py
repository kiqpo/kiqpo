import os

def ReadJS(file='/core.js'):
    NativeDIR = os.getcwd()+'/native'
    data = open(NativeDIR+file, 'r')
    return data.read()
