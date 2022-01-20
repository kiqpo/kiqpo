from view import *


def RunApp():
    Head(),
    Body(
        TopNav(backgroundColor='#fff', labelText='dev'),
        Builder(Content=Text('hello'), count=10)
    )
