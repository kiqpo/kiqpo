from view import *


def RunApp():
    Head(title="Welcome"),
    Body(
        BottomNav(),
        Text("Hello, there! 👋. Thanks for checking out Bionic web framework amogst all other frameworks. To get started checkout the bionic documentation at https://bionic-py.github.io/Bionic-Documentation/."),
        Button(text="btn", classname='btn'),

    ),
