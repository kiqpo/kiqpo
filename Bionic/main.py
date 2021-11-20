from view import *


def RunApp():
    Head(title="Welcome"),
    Body(
        BottomNav(),
        Text("Hello, there! 👋. Thanks for checking out Bionic web framework amogst all other frameworks. To get started checkout the bionic documentation."),
        Button(text="btn", classname='btn'),

    ),
