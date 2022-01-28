from view import *

def RunApp():
    # head tag
    Head(title="Kiqpo", themeColor="#ffffff"),
    Body(
        # navbar at the top.
        TopNav(backgroundColor="#ffffff", labelgap="3%", label=Text(
            "Kiqpo", TextStyle=TextStyle(
                Color='green',
                FontSize='220%',
                Weight='900'),
        )),

        # text with padding
        Padding(child=Text('Hello from kiqpo.', TextStyle=TextStyle(
            FontSize="160%",
            Color="#292827",
            Weight='900'
        )), top='0.5%', left="1%"),

        # text with padding & sub heading
        Padding(child=Text('Runing in kiqpo in', Id="platform", TextStyle=TextStyle(
            FontSize='85%',
            Weight="550"
        )), top='0%', left="1%")
    ),