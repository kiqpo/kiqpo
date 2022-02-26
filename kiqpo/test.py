from view import *


def RunApp():
    Head(),
    Body(
        TopAppBar(Title='kiqpo'),
        SafeArea(
            Padding(
                Div(
                    Text('Hello from kiqpo', TextStyle=TextStyle(
                        FontSize=Screen(175),
                        Color=Colors.gray[500],
                        Weight='600'
                    )),
                    Padding(
                        Text("New account", TextStyle=TextStyle(
                            Color=Colors.gray[100]
                        )),
                        top=Px(4),
                        bottom=Px(10)
                    ),
                    Padding(
                        IconButton(
                            text='Login with email',
                            icon=Icons.email,
                            onTap=Alert("login with email"),
                            style=buttonstyle(
                                 background=Colors.red,
                            )), top=Px(20)),

                    Padding(
                        IconButton(
                            text='Login with face',
                            icon=Icons.face,
                            onTap=Alert("login with face"),
                            style=buttonstyle(
                                background=Colors.green,
                            )), top=Px(20)),
                ),
            ),
        ),
    )