import eel

# this can be called from js.
# my_python_function.


@eel.expose
def my_python_function():
    print('hey')


@eel.expose
def add(a, b):
    print(a+b)


eel.init('../native')
eel.start('index.html')
