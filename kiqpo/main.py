from view import*


def RunApp():
    Head(),
    Body(
        KiqpoLayout(
            TopAppBar(title='My app', style=TopAppBarStyle(
                background=Colors.blue
            )),
            Home(
                Padding(
                    Button(label='blue button', style=buttonstyle(
                        borderRadius=Px(5),
                        width=Screen(19),
                        background=Colors.blue
                    ), onTap=Alert("hello")),
                ),
                Padding(
                    Button(label='red button', style=buttonstyle(
                        borderRadius=Px(5),
                        width=Screen(19),
                        background=Colors.red
                    ), onTap=Snackbar.show("MySnackbar",'HI to python')),
                ),
                Snackbar.initialize("MySnackbar"),
            ),
        ),
    )
