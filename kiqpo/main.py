from view import *


def RunApp():
    Head(title="Netflix", themeColor="#000000"),
    Body(
        TopNav(backgroundColor="#000000", labelgap="3%", label=Text(
            "Netflix", TextStyle=TextStyle(
                Color='red',
                FontSize='220%',
                Weight='900'
            ),
        )),
        Padding(child=Text('welcome to Netflix-India', TextStyle=TextStyle(
            FontSize="100%"
        ))),
    ),
