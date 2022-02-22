from view import *


def account():
    return Div(Padding(
        Flex(
            Text("Account settings", TextStyle=TextStyle(FontSize=Screen(290), Weight='900')),
            Text("shajin_sha", TextStyle=TextStyle(Weight='500'))),
    ),classname="Account")
