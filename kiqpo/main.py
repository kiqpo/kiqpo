from view import *
from pages import home, account


def RunApp():
    Head(),
    Body(
        Window(home.home(), account.account()),
        setTheme(),
        SafeArea(
            TopNav(Title="kiqpo"),
            Padding(
                IconButton(
                    text='account',
                    icon=Icons.account_circle,
                    onTap=Navigator('account', 1, 'account settings', 'Home'))),
            Padding(
                IconButton(text='home',
                           icon=Icons.home,
                           onTap=Navigator('home', 0, 'home', 'Account'))),
        ),
    )
