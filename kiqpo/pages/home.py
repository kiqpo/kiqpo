from view import *


def home():
    return Div(Padding(
        Flex(
            Text("Welcome", TextStyle=TextStyle(FontSize=Screen(290), Weight='900')),
            Text("shajin_sha", TextStyle=TextStyle(Weight='500'))),
    ),classname="Home")
