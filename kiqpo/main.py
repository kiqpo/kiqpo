from view import *
from pages import home, user


def RunApp():
    Head(),
    Body(
        TopNav(Title="Kiqpo"),
        Window(home.Home(), user.user()),
        SafeArea(
            Navigate("user-page", 1, "User", 'Home-page'),
            Navigate("home-page", 0, "Home", 'User-page'),

        ),
    ),
