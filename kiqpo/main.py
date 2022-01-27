from view import *


def RunApp():
    Head(title="Kiqpo", themeColor="#ffffff"),
    Body(
        TopNav(backgroundColor="#ffffff", labelgap="3%", label=Text(
            "Kiqpo", TextStyle=TextStyle(
                Color='green',
                FontSize='220%',
                Weight='900'),
        )),
        Padding(child=Text('Hello from kiqpo.', TextStyle=TextStyle(
            FontSize="160%",
            Color="#292827",
            Weight='900'
        )), top='0.5%', left="1%"),
        Padding(child=Text('Runing in kiqpo in', Id="platform", TextStyle=TextStyle(
            FontSize='85%',
            Weight="550"
        )), top='0%', left="1%")
    ),
