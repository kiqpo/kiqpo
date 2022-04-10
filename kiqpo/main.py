from view import*


def RunApp():
    Head(),
    Body(
        KiqpoLayout(
            TopAppBar(Title="Kiqpo"),
            Home(
                Text("Hello from Kiqpo", Type='H2'),
                Padding(IconButton(icon=Icons.file_download, text='hello'))
            ),
        )
    )
